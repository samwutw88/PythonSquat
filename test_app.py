import requests
import time
import subprocess
import signal
import os

def test_app():
    # 啟動 Flask 應用
    app_process = subprocess.Popen(['python', 'app.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # 等待應用啟動
    time.sleep(2)

    base_url = 'http://localhost:5000'

    try:
        # 測試 1: GET /
        print("Testing GET /")
        response = requests.get(f'{base_url}/')
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text[:100]}...")  # 只顯示前100字
        assert response.status_code == 200
        assert 'Hello' in response.text

        # 測試 2: GET /item/apple
        print("\nTesting GET /item/apple")
        response = requests.get(f'{base_url}/item/apple')
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        assert response.status_code == 200
        assert response.json()['item']['name'] == 'apple'

        # 測試 3: POST /item/banana
        print("\nTesting POST /item/banana")
        data = {'price': 15.5}
        response = requests.post(f'{base_url}/item/banana', json=data)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        assert response.status_code == 201
        assert response.json()['name'] == 'banana'

        # 測試 4: GET /items
        print("\nTesting GET /items")
        response = requests.get(f'{base_url}/items')
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        assert response.status_code == 200
        assert len(response.json()['items']) >= 2  # apple and banana

        # 測試 5: POST /squat
        print("\nTesting POST /squat")
        squat_data = {'exercise': 'squat', 'reps': 10}
        response = requests.post(f'{base_url}/squat', json=squat_data)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        assert response.status_code == 200
        # 檢查回應包含添加的字段
        resp_data = response.json()
        assert 'empid' in resp_data
        assert 'skey' in resp_data
        assert 'createdate' in resp_data

        print("\nAll tests passed!")

    except Exception as e:
        print(f"Test failed: {e}")
        raise
    finally:
        # 停止應用
        app_process.terminate()
        app_process.wait()

if __name__ == "__main__":
    test_app()