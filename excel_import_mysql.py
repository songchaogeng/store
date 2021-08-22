import xlrd
import pymysql

file=xlrd.open_workbook("2020年每个月的销售情况.xls")
con=pymysql.connect(host="localhost",user="root",password="123456",database="excel")
cursor=con.cursor()


#给读取的表定义一个循环变量
temp=0
month=['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
for i in month:
    sql_create_table = "CREATE TABLE if not exists " + i + " (`日期` VARCHAR(10),`服装名称` VARCHAR(10),`价格/件` FLOAT,`本月库存数量` FLOAT,`销售量/每日` FLOAT)"
    cursor.execute(sql_create_table)
    con.commit()
    sheet = file.sheet_by_index(temp)
    for row in range(1,sheet.nrows):
        date = sheet.row_values(row)
        sql_insert = "insert into " + i + " values (%s,%s,%s,%s,%s)"
        param1 = date
        cursor.execute(sql_insert, param1)
        con.commit()
    temp = temp+1
cursor.close()
con.close()