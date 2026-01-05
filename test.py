import requests
import mysql.connector

config = {
    'user': 'labuser39',          # 사용자 이름
    'password': 'Onetwothree-0',      # 비밀번호
    'host': 'labuser39-mysql.mysql.database.azure.com',              # 호스트 주소 (보통 localhost)
    'database': 'classicmodels'  # 데이터베이스 이름
}

def fetch_table_data():

    connection = None
    try:
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            cursor = connection.cursor()
            
            # 3. SQL 쿼리 실행 (특정 테이블 이름 입력)
            table_name = "employees"
            query = f"SELECT * FROM {table_name}"
            cursor.execute(query)
            
            # 4. 결과 가져오기
            rows = cursor.fetchall()
            
            print(f"총 {len(rows)}개의 데이터를 가져왔습니다.\n")
            
            # 5. 데이터 출력
            for row in rows:
                print(row)
                
    except mysql.connector.Error as err:
        print(f"오류 발생: {err}")
        
    finally:
        # 6. 연결 종료
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("\n데이터베이스 연결이 종료되었습니다.")

fetch_table_data()