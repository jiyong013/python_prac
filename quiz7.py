
for week in range(1,51) :
    with open("{0}주차.txt".format(week), 'w', encoding='utf8') as weekly_report:
        weekly_report.write("- {0} 주차 주간보고 -\n".format(week))
        weekly_report.write("부서 :\n")
        weekly_report.write("이름 :\n")
        weekly_report.write("업무 요약 :\n")


        

