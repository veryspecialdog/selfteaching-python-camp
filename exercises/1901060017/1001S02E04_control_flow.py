for n in range(1,10):                                    #分别取出1~9十个数字，并且把每个数字赋值给n
        for i in range(1,n+1):                           #分别取出1~n+1的数字，并且把每个数字复制给i
                print(f'{n}*{i}={n*i}',end='\t')         #在终端输出运算公式和结果，并且去掉换行符
        print()                                          #打印之后进行换行



#n=1                                                     #给变量n赋值等于1                                       
#while n < 10 :                                          #判断n小于10的时候执行while语句
#        for i in range(1,n+1):                          #取出1到n+1的每一个数字并且复制给i
#                if n % 2 != 0:                          #判断当n为奇数是在之下print语句
#                        print(f'{n}*{i}={n*i}',end='\t')#输出公式和结果，并且去掉换行符
#        n+=1                                            #每执行一次程序，n的值都+1       
#        print()                                         #打印后换行