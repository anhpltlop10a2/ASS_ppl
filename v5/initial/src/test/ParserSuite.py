# import unittest
# from TestUtils import TestParser

# class ParserSuite(unittest.TestCase):
    
#     def test_0(self):
#         """Return + Continue"""
#         input = """
#         Function: main
#         Body:
#         Var: a[5][5+2] = {1,2,3,{1,2,3}} **array_declare**; 
#         Return a; 
#         EndBody. 
#         """
#         expect = "Error on line 4 col 19: +"
#         self.assertTrue(TestParser.checkParser(input,expect,0))
#     def test_simple_program(self):
#         """Simple program: int main() {} """
#         input = """Var: x;"""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,1))
#     def test_wrong_miss_close(self):
#         """Miss variable"""
#         input = """Var: ;"""
#         expect = "Error on line 1 col 5: ;"
#         self.assertTrue(TestParser.checkParser(input,expect,2))
#     def test_missing_close(self):
#         input = """ Var: a[10][8] = {1,2,{1,0.1}}, b = 8, c; """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,3))
#     def test_4(self):
#         input = """ Var: hi,a = {True,False,\"h\"}, d = True, k = False, c = \"abc\"; """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,4))
#     def test_5(self):
#         """comment"""
#         input = """ Var: **tiivicnivihivhirfijirjifieji** l,b **fhudh**,c = {1,2},a = \"a **i**\"; """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,5))
#     def test_6(self):
#         input = """ Var: m, k , i = {1,2},8;"""
#         expect = "Error on line 1 col 23: 8"
#         self.assertTrue(TestParser.checkParser(input,expect,6))
#     def test_7(self):
#         """"Var khong co hai cham"""
#         input = """ Var giugin,c = {7,8,9,{7,4,5}},y;"""
#         expect = "Error on line 1 col 5: giugin"
#         self.assertTrue(TestParser.checkParser(input,expect,7))
#     def test_8(self):
#         input = """ Var: exp,a,c = True,a;"""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,8))
#     def test_9(self):
#         input = """ Var: hi,a,c = 1 + 8 ;"""
#         expect = "Error on line 1 col 17: +"
#         self.assertTrue(TestParser.checkParser(input,expect,9))
#     def test_10(self):
#         input = """ Var: foo(2),a,c = 1 + 8 ;"""
#         expect = "Error on line 1 col 9: ("
#         self.assertTrue(TestParser.checkParser(input,expect,10))
#     def test_11(self):
#         input = """ Var: ,j,l,p = (1 + 8) ;"""
#         expect = "Error on line 1 col 6: ,"
#         self.assertTrue(TestParser.checkParser(input,expect,11))
#     def test_12(self):
#         """Phan ve phai cua Var chi la LIT khong dc EXP """
#         input = """ Var: def = (1 + 8) ;"""
#         expect = "Error on line 1 col 12: ("
#         self.assertTrue(TestParser.checkParser(input,expect,12)) 
#     def test_13(self):
#         input = """ Var: \"b\",p,k,i = iostream;""" 
#         expect = "Error on line 1 col 6: b"
#         self.assertTrue(TestParser.checkParser(input,expect,13))
#     def test_14(self):
#         """Khong dc gan bang ID ma chi dc LIT"""
#         input = """ Var: j = k ;"""
#         expect = "Error on line 1 col 10: k"
#         self.assertTrue(TestParser.checkParser(input,expect,14))
#     def test_15(self):
#         input = """ Var: def = d[5] ;"""
#         expect = "Error on line 1 col 12: d"
#         self.assertTrue(TestParser.checkParser(input,expect,15))
#     def test_16(self):
#         """thieu ; """
#         input = """ Var: test"""
#         expect = "Error on line 1 col 10: <EOF>"
#         self.assertTrue(TestParser.checkParser(input,expect,16))
#     def test_17(self):
#         """thieu ; """
#         input = """ Var _param;"""
#         expect = "_"
#         self.assertTrue(TestParser.checkParser(input,expect,17))
#     def test_18(self):
#         input = """ Var: $$a = 8;"""
#         expect = "$"
#         self.assertTrue(TestParser.checkParser(input,expect,18))
#     def test_19(self):
#         input = """ Var: 1 = 8;"""
#         expect = "Error on line 1 col 6: 1"
#         self.assertTrue(TestParser.checkParser(input,expect,19))
#     def test_20(self):
#         input = """ Var: {a,v} = 8;"""
#         expect = "Error on line 1 col 6: {"
#         self.assertTrue(TestParser.checkParser(input,expect,20))
#     def test_21(self):
#         """Parameter khong dc gan"""
#         input = """ Var: m, n = 0.5, k = 10.01e+4;
#         Function: main
#         Parameter: x = 8,y,a[5]
#         Body:
#             x = x +1; 
#         EndBody."""
#         expect = "Error on line 3 col 21: ="
#         self.assertTrue(TestParser.checkParser(input,expect,21))
#     def test_22(self):
#         """Unterminated Cmt"""
#         input = """ Var: i = 8, m, n, k;
#         Function: test_demo
#         Parameter: x,y,z**huhucuocsongkhoquama
#         Body:
#         EndBody."""
#         expect = ""
#         self.assertTrue(TestParser.checkParser(input,expect,22))
#     def test_23(self):
#         input = """ Var: test, demo = 0.5;
#         Function: test_15
#         Parameter: m,l,j
#         Body:
#             Var: m = 5, b[2][8] = {1,5,5}; 
#         EndBody."""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,23))
#     def test_24(self):
#         input = """ Var: m, n = {1,5,9}, k = 10.01e+4;
#         Function: test_15
#         Parameter: x,y,z
#         Body:
#             x = x > 2; 
#             If (foo(2) > 3) || (y >= 10) Then x = x + 2; EndIf.
#             While ((p != 2) && (z > 3)) Do **nothing** EndWhile.
#         EndBody."""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,24))
#     def test_25(self):
#         input = """ Var: a = 8 ;
#         Function: test_demo
#         Parameter: x,y,z
#         Body:
#         a [^ ^]= 52 ; 
#         EndBody."""
#         expect = "^"
#         self.assertTrue(TestParser.checkParser(input,expect,25))
#     def test_26(self):
#         """Bieu thuc"""
#         input = """ Var: a = {1,2,0xFF} , b = \"**hi\", c ;
#         Function: main
#         **main ne**
#         Parameter: x,y,z
#         **Param **
#         Body:
#         If foo(2) Then x = x + 2; EndIf.
#         a[3 + foo(2)] = {1,2,0};
#         a = (a+b*foo(8));
#         a = "uit";
#         go("a"); 
#         EndBody."""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,26))
#     def test_27(self):
#         """main + func"""
#         input = """ Var: a = 2; 
#         Function: main
#         Parameter: a
#         Body:
#         y = \"a\"; 
#         z[foo(2)*3] = {1.5,9};
#         k[(a)] = 5;
#         a[10+foo(2)][8] =  a(9);  
#         foo(2); 
#         EndBody.
#         Function: abc
#         Parameter: a
#         Body:
#         y = True; 
#         a[10+foo(2)][8] =  a(9);  
#         foo(2); 
#         EndBody."""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,27))
#     def test_28(self):
#         """Trong ham k co stm"""
#         input = """ Var: a = {1,2,0xFF} , b = \"**hi\", c ;
#         Function: main
#         **main ne**
#         Parameter: x,y,z
#         **Param **
#         Body:
#         ** null stm **
#         EndBody."""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,28))
#     def test_29(self):
#         """Trong ham co stm + Phep index co exp"""
#         input = """  Var: a = {1,2};
#         Function: main
#         Parameter: a
#         Body:
#         arr[\"a\"][!9]= 8; 
#         EndBody.
#         Function : abc
#         Body:
#         a = 2 ;   
#         If foo(2) Then x = x + 2; EndIf.
#         a[3 + foo(2)] = {1,2,0};
#         a = (a+b*foo(8));
#         a = \"uit\";
#         go(\"a\"); 
#         EndBody."""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,29))
#     def test_30(self):
#         """exp trong index"""
#         input = """ 
#         Var: a = 8 ;
#         Function: test_demo
#         Parameter: x,y,z
#         Body:
#         Var : b = {1,\"update\",5,{0.5,0xFF}};
#         a [a + 2+ a[2]][foo(2)+2]= 52 ; 
#         EndBody."""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,30))
#     def test_31(self):
#         input = """ 
#         Var: k = 5, m = {2,5} ;
#         Function: test_demo
#         Parameter: x,y,z
#         Body:
#         a[1.2+6] = (5+2) ; 
#         EndBody."""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,31))
#     def test_32(self):
#         """If statement"""
#         input = """ 
#         Var: j,k,i;
#         Function: func
#         Parameter: bkit
#         Body:
#             a = 8; 
#             If (m\\8 =/= y % 5) Then a = {1,2,3}; EndIf.
#         EndBody."""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,32))
#     def test_33(self):
#         """if elseif else"""
#         input = """ 
#         Function: nam
#         Parameter: x,y,a[20]
#         Body:
#             If(i == term) Then
#                 For(i=8,i<15,i-5) Do
#                 x=x+y;
#                 r && 8; 
#                 EndFor.
#             ElseIf (True) Then
#                 **do nothing**
#             Else 
#             a=b+d;
#             foo(2);
#             EndIf.
#         EndBody."""
#         expect = "Error on line 8 col 18: &&"
#         self.assertTrue(TestParser.checkParser(input,expect,33))
#     def test_34(self):
#         input = """ 
#         Function: nam
#         Parameter: x,y,a[20]
#         Body:
#             If(i == term) Then
#             **donothing**
#             EndIf.
#         EndBody."""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,34))
#     def test_35(self):
#         """for khong co ngoac"""
#         input = """
#         Function: hi
#         Body:
#         For i=1, i<2, n++ Do
#             If i % 2 == 0 Then write(i);
#             dem:=dem+1;
#             EndFor.
#             If dem = 15 Then
#             dem:=0;
#             writeln(dem); 
#             EndIf.
#         EndFor.
#         readln();
#         EndBody. 
#         """
#         expect = "Error on line 4 col 12: i"
#         self.assertTrue(TestParser.checkParser(input,expect,35))
#     def test_36(self):
#         """for  co ngoac nhung bi :="""
#         input = """
#         Function: hi
#         Body:
#         For (i=1, i<2, n+1) Do
#             If i % 2 == 0 Then write(i);
#             dem : =dem+1;
#             EndFor.
#             If dem = 15 Then
#             dem:=0;
#             writeln(dem); 
#             EndIf.
#         EndFor.
#         readln();
#         EndBody. 
#         """
#         expect = "Error on line 6 col 16: :"
#         self.assertTrue(TestParser.checkParser(input,expect,36))


#     def test_37(self):
#         """Return + Continue"""
#         input = """
#         Function: loop
#         Body:
#         If 2 Then i = 0; EndIf.
#         readln();
#         Return a;
#         For (i=1, 2 +3 , 5+6) Do 
#             Return foo(2) + 8 \\a[5]; 
#             If 2 Then i = 0; EndIf.
#             Break;
#             If i % 2 Then 
#                 write(i);
#                 dem = dem + 1 ; 
#                 While t(1) Do 
#                     Return t(1) + t(n-1); 
#                     Break;
#                 EndWhile.
#             EndIf.  
#             Return a;
#             Continue; 
#         EndFor.
#         EndBody. 
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,37))
    

#     def test_38(self):
#         """Break khong nam trong loop"""
#         input = """
#         Function: main
#         Body:
#         If 2 Then i = 0; EndIf.
#         readln();
#         Return a;
#         For (i=1, 2 +3 , 5+6) Do 
#             Return foo(2) + 8 \\a[5]; 
#             If 2 Then i = 0; EndIf.
#             Break;
#             If i % 2 Then 
#                 write(i);
#                 dem = dem + 1 ; 
#                 While t(1) Do 
#                     Return t(1) + t(n-1); 
#                     Break;
#                 EndWhile.
#             EndIf.  
#             Return a;
#             Continue; 
#         EndFor.
#         Break;
#         EndBody. 
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,38))
    
#     def test_unbunary_Mul_exp(self):
#         input = """
#         Function: exp_fail
#         Body:
#         For (i=1, 2 +3 , 5+6) Do 
#         a [5+foo(2)][g+8] = a[a+b[0]\\5] ;
#         b = a *;
#         EndFor.
#         EndBody. 
#         """
#         expect = "Error on line 6 col 15: ;"
#         self.assertTrue(TestParser.checkParser(input,expect,39))
#     def test_sign(self):
#         input = """
#         Function: sign
#         Body:
#         a = a \. 2;
#         c[5][5] = foo(3+foo(2)) + True; 
#         a[5] = True || False; 
#         m = True-.True;
#         EndBody. 
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,40))
#     def test_do_while(self):
#         input = """
#         Function: test
#         Body:
#         Do
#         a = a \. 2;
#         c[5][5] = foo(3+foo(2)) + True; 
#         a[5] = True || False; 
#         m = True-.True;
#         While a && True
#         EndDo.
#         EndBody. 
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,41))
#     def test_wrong_return_with_assign(self):
#         input = """
#         Function: test2
#         Body:
#         Do
#         Continue; 
#         Return z = (a % 2)*8;
#         c[5][5] = foo(3+foo(2)) + True; 
#         a[5] = True || False; 
#         m = True-.True;
#         Break; 
#         While a && True
#         EndDo.
#         EndBody. 
#         """
#         expect = "Error on line 6 col 17: ="
#         self.assertTrue(TestParser.checkParser(input,expect,42))
#     def test_43(self):
#         """Trong For ID = Int_lit"""
#         input = """
#         Var: b = 8, c = 0xFF, d= {1,9,10}; 
#         Function: test43
#         Parameter: p, v
#         Body:
#         Var: foo = 5;
#         Do
#             Continue;
#             Return (p*v)\\(r*t);
#             If a - 8 Then z = z + z*2; 
#             ElseIf **elseif** foo(9+foo(4)\\foo(3)*5)  Then **for in if**
#                 For (f =  l + 8, f,f)
#                 Do 
#                     f = f + 2; 
#                     k = k + k[10][100]; 
#                 EndFor.
#             EndIf.
#             Break; 
#         While a && True
#         EndDo.
#         EndBody. 
#         """
#         expect = "Error on line 12 col 26: l"
#         self.assertTrue(TestParser.checkParser(input,expect,43))
#     def test_44(self):
#         """Trong index"""
#         input = """
#         Var: b = 8, c = 0xFF, d= {1,9,10}; 
#         Function: test43
#         Parameter: p, v
#         Body:
#         Do 
#             If a - 8 Then z = z + z*2; 
#             ElseIf **elseif** foo(9+foo(4)\\foo(3)*5)  Then **for in if**
#             EndIf.
#             For (f = 8, m ,foo(2)+ 8*2)
#             Do 
#                 Break; 
#                 f = f + 2; 
#                 k = k + k[10][100]; 
#                 Break;
#                 Continue; 
#             EndFor.   
#         m=m[b[5+5*.0.2][2]];
#         While foo(2) + 8 *2 
#         EndDo.
#         EndBody. 
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,44))
#     def test_45(self):
#         input = """ Function: main
#         Parameter: y,z,a
#         Body:
#         While fun() == True Do process(currentNode); 
#         EndWhile.
#         If currentNode_left == null Then enqueue(bfQueue, currentNode_left);
#         EndIf.
#         If currentNode_right != null Then enqueue(bfQueue, currentNode_right);
#         EndIf.
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,45))
#     def test_46(self):
#         """Miss variable"""
#         input = """
#     Var: a,b[5]; 
#     Function: main
#     Parameter: p,x
#     Body:
#     If root == valid Then root = newPtr; ElseIf foo(5) Then 
#         foo(6); 
#         taller = true;
#         Return root; 
#     EndIf.
#     EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,46))
    
#     def test_47(self):
#         """Miss variable"""
#         input = """
#         Var: a,b,c,cv,dt,p=8;
#         Function: square
#         Parameter: d, r
#         Body: 
#             Return a; 
#             write(\"a\" =/= 8);
#             Return b; 
#             write(\"b\" + b);
#             Return square == a * b ; 
#             write(square); 
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,47))
#     def test_48(self):
#         """Miss variable"""
#         input = """
#         Var: a,b,tmp;
#         Function: swap_a_b
#         Parameter: a,b 
#         Body: 
#             If a>b Then
#             tmp=a;
#             a=b;
#             b=tmp;
#             EndIf.
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,48))
#     def test_49(self):
#         input = """
#         Var: root,left = 4, a = {4,True,5,{False,0xFF,0o47}};
#         Function: giaithua
#         Parameter: n
#         Body: 
#             If n == 1 Then
#                 Return 1;
#             Else Return n * giaithua(n-1);
#             EndIf. 
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,49))
#     def test_param_missing_var_close(self):
#         input = """
#         Var: root,left = 4,a;
#         Function: id
#         Parameter: n,a,b
#         Body: 
#             For (i=1, i<100, i+2) Do
#                 Continue; 
#                 Break; 
#                 Break; 
#                 Return (n -1)*2;
#                 a = a * i; 
#                 b = b - i; 
#                 n = a + b; 
#                 Break;
#                 Continue; 
#                 Break;
#             EndFor.
#             Return a; 
#             Return b; 
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,50))
#     def test_51(self):
#         input = """
#         Function: fibo
#         Parameter: n
#         Body: 
#             If (n == 1) || (n ==2) Then Return 1;
#             Else Return fibonacci(n - 1) + fibonacci(n - 2);
#             EndIf.
#         EndBody.
#         Function: main
#         Parameter: n
#         Body:
#             print (\"nhap n: \");
#             cout (\"So fibonacci thu Fibonacci(n)\");
#             Return 0;
#         EndBody.
        
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,51))
#     def test_52(self):
#         input = """
#         Function: fibo
#         Parameter: n
#         Body: 
#             a = -a + 8;
#             If n%2 == 0 Then Return 1;
#             EndIf.
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,52))
#     def test_54(self):
#         input = """
#         Function: composit_Expression
#         Parameter: n
#         Body: 
#             While 5*.2+.5 Do 
#                 Break;
#                 If n%2 == 0 Then a = a[foo(2) +5 *.5]; EndIf.
#             EndWhile. 
#             Do 
#                 p = arr[a[5] + a [foo(2) % 5 \. 9]] ;
#                 Break; 
#                 Continue; 
#             While arr[5] *. 8
#             EndDo.
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,54))
    
#     def test_55(self):
#         """Test Exp"""
#         input = """Var: a[5] = {5,6} ; 
#         Function: main
#         Body:
#             foo = foo(5+7,2,foo(2)+8)[1][\"a\"**hi**];
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,55))
#     def test_56(self):
#         """Test Exp"""
#         input = """Var: a[5] = {5,6} ; 
#         Function: main
#         Body:
#             foo = foo(5+7,2,foo(2)+8)[1][\"a\"**hi**];
#         EndBody.
#         Function: id_1
#         Parameter: f
#         Body: 
#             Var: a= {1,2,3}; 
#             foo(arr[5] *. 5,True,\"abc\"); 
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,56))
#     def test_57(self):
#         """Khong dc Var sau func"""
#         input = """Var: a[5] = {5,6} ; 
#         Function: a
#         Parameter: f
#         Body: 
#             foo(arr[5] *. 5,True,\"abc\"); 
#             Var: a= {1,2,3}; 
#         EndBody.
#         Function: main
#         Body:
#             foo = foo(5+7,2,foo(2)+8)[1][\"a\"**hi**];
#         EndBody.
#         Function: id_1
#         Parameter: f
#         Body: 
#             Var: a= {1,2,3}; 
#             foo(arr[5] *. 5,True,\"abc\"); 
#         EndBody.
#         """
#         expect = "Error on line 6 col 12: Var"
#         self.assertTrue(TestParser.checkParser(input,expect,57))
#     def test_58(self):
#         input = """Var: a[5] = {5,6} ; 
#         Function: a
#         Parameter: f
#         Body: 
#             Var: a = {1,2,3}, b = \"abc\"; 
#             foo(arr[5] *. 5,True,\"abc\"); 
#             If (h && k && t + 8) Then a = 1; EndIf. 
#             Do a = a[5]; 
#             While c - 5
#             EndDo.   
#         EndBody.
#         Function: main
#         Body:
#             foo = foo(5+7,2,foo(2)+8)[1][\"a\"**hi**];
#         EndBody.
#         Function: id_1
#         Parameter: f
#         Body: 
#             Var: a = {1,2,3}; 
#             foo(arr[5] *. 5,True,\"abc\"); 
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,58))
#     def test_59(self):
#         input = """Var: a[5] = {5,6} ; 
#         Function: a
#         Parameter: f
#         Body: 
#             Var: a = {1,2,3}, b = \"abc\"; 
#             foo(arr[5] *. 5,True,\"abc\"); 
#             If (h * 5 && k && t + 8) Then a = 1; EndIf. 
#             Do a = a[5]; 
#             While c - 5
#             EndWhie.   
#         EndBody.
#         """
#         expect = "Error on line 10 col 12: EndWhile"
#         self.assertTrue(TestParser.checkParser(input,expect,59))
#     def test_59(self):
#         input = """Var: a[5] = {5,6} ; 
#         Function: a
#         Parameter: f
#         Body: 
#             Var: a = {1,2,3}, b = \"abc\"; 
#             foo(arr[5] *. 5,True,\"abc\"); 
#             If (h * 5 && k && t + 8) Then a = 1; EndIf. 
#             Do a = a[5]; 
#             While a + 4
#             EndWhile.   
#         EndBody.
#         """
#         expect = "Error on line 10 col 12: EndWhile"
#         self.assertTrue(TestParser.checkParser(input,expect,59))
#     def test_60(self):
#         input = """Var: a[5] = {5,6} ; 
#         Function: a
#         Parameter: f
#         Body: 
#             Var: a = {1,2,3}, b = \"abc\"; 
#             foo(arr[5] *. 5,True,\"abc\"); 
#             If (h * 5 && k && t + 8) Then a = 1; ElseIf e >=. 8 Then **donothing** EndIf. 
#             Do a = a[5]; 
#             While c - 5
#             EndDo.   
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,60))
#     def test_61(self):
#         input = """Var: a[5] = {5,6} ; 
#         Function: a
#         Parameter: f
#         Body: 
#             Var: a = {1,2,3}, b = \"abc\"; 
#             foo(arr[5] *. 5,True,\"abc\"); 
#             If (h * 5 && k && t + 8) Then a = 1; ElseIf e >=. 8 Then **donothing** EndIf. 
#             Do a = a[5]; 
#             While c - 5
#             EndDo.   
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,61))
#     def test_62(self):
#         """Thieu EndIf"""
#         input = """Var: a[5] = {5,6} ; 
#         Function: a
#         Parameter: f
#         Body: 
#             Var: a = {1,2,3}, b = \"abc\"; 
#             foo(arr[5] *. 5,True,\"abc\"); 
#             If (h * 5 && k && t + 8) Then a = 1; ElseIf e >=. 8 Then **donothing** EndIf. 
#             Do 
#                 a = a[5]; 
#                 If arr[5][9+foo(8)*2] Then **nothing**
#             While c - 5
#             EndDo.   
#         EndBody.
#         """
#         expect = "Error on line 11 col 12: While"
#         self.assertTrue(TestParser.checkParser(input,expect,62))
#     def test_63(self):
#         input = """Var: a[5] = {5,6} ; 
#         Function: a
#         Parameter: f
#         Body:  
#             foo(arr[5] *. 5,True,\"abc\"); 
#             If running(h =/= 9,\"a\") Then a = 1; ElseIf e >=. 8 Then **donothing** EndIf. 
#             Do 
#                 If (a + 0xFF) Then running(root); EndIf.
#                 While foo(9 + a[10]) Do 
#                     If (a + 0xFF) Then running(root); EndIf.
#                 EndWhile.
#                 a = a[5]; 
#                 u (\"a\" && 8); 
#                 While c*8 
#                 Do
#                 EndWhile.
#             While foo(8)
#             EndDo.   
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,63))
#     def test_64(self):
#         """Thieu EndIf truoc EndWhile"""
#         input = """Var: a[5] = {5,6} ; 
#         Function: a
#         Parameter: f
#         Body:  
#             foo(arr[5] *. 5,True,\"abc\"); **foo()**
#             If running(h =/= 9,\"a\") Then a = 1; **para** ElseIf e >=. 8 Then **donothing** EndIf. 
#             Do 
#                 If (a + 0xFF) Then running(root); EndIf.
#                 While foo(9 + a[10]) Do 
#                     If (a + 0xFF) Then running(root);  **if staement**
#                 EndWhile.
#                 a = a[5]; 
#                 u (\"a\" && 8); 
#                 While c*8 
#                 Do
#                 EndWhile.
#             While foo(8)
#             EndDo.   
#         EndBody.
#         """
#         expect = "Error on line 11 col 16: EndWhile"
#         self.assertTrue(TestParser.checkParser(input,expect,64))
#     def test_65(self):
#         input = """Var: a[5] = {5,6,\"abc\"} ; 
#         Function: a
#         Parameter: f
#         Body:  
#             foo(arr[5] *. 5,True,\"abc\"); 
#             If running(h =/= 9,\"a\") Then a = 1; ElseIf e >=. 8 Then **donothing** EndIf. 
#             Do 
#                 If (a + 0xFF) Then running(root); EndIf.
#                 While foo(9 + a[10]) Do 
#                     If (a + 0xFF) Then running(root); EndIf.
#                 EndWhile.
#                 a = a[5]; 
#                 u (\"a\" && 8); 
#                 While c*8 
#                 Do
#                 EndWhile.
#             While foo(8)
#             EndDo.   
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,65))
#     def test_66(self):
#         input = """Var: a[5] = {5,6,\"abc\"}, t = True, b = False ; 
#         Function: a
#         Parameter: f
#         Body:  
#             foo(\"abc\" && \"xyz\"); 
#             If running(root) Then a = 1; ElseIf e >=. 8 Then
#                 Do 
#                     While foo(\"neunhungayay\") Do 
#                         If (a + 0xFF) Then running(root); EndIf.
#                         Return a - 8; 
#                     EndWhile.
#                     If (a + 0xFF) Then running(root); EndIf.
#                     a = a[5]; 
#                     u (\"a\" && 8); 
#                     While c*8 
#                     Do 
#                         If (9 + 10e9) Then 
#                             running(root_left); 
#                             a = 10 - 8 ; 
#                         EndIf.    
#                     EndWhile.
#                 While c - a[5]
#                 EndDo.   
#             EndIf. 
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,66))
#     def test_67(self):
#         input = """Var: a[5] = {5,6,\"abc\"}, t = True, b = False ; 
#         Function: a
#         Parameter: f
#         Body:  
#             foo(\"abc\" && \"xyz\"); 
#             If running(root) Then a = 1; ElseIf e >=. 8 Then
#                 Do 
#                     While foo(\"neunhungayay\") Do 
#                         If (a + 0xFF) Then running(root); EndIf.
#                         Return a - 8; 
#                     EndWhile.
#                     If (a + 0xFF) Then running(root); EndIf.
#                     a = a[5]; 
#                     u (\"a\" && 8); 
#                     While c*8 
#                     Do 
#                         If (9 + 10e9) Then 
#                             running(root_left); 
#                             a = 10 - 8 ; 
#                             Return x - y ; 
#                         EndIf.    
#                     EndWhile.
#                 While c - a[5]
#                 EndDo.   
#             EndIf. 
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,67))
#     def test_68(self):
#         input = """Var: a[5] = {5,6,\"abc\"}, t = True, b = False ; 
#         Function: a
#         Parameter: f
#         Body:  
#             foo(\"abc\" && \"xyz\"); 
#             If running(root) Then a = 1; ElseIf e >=. 8 Then
#                 Do 
#                     While foo(\"neunhungayay\") Do 
#                         If (a + 0xFF) Then running(root); EndIf.
#                         Return a - 8; 
#                     EndWhile.
#                     If (a + 0xFF) Then running(root); EndIf.
#                     a = a[5]; 
#                     u (\"a\" && 8); 
#                     While c*8 
#                     Do 
#                         If (9 + 10e9) Then 
#                             running(root_left); 
#                             a = 10 - 8 ; 
#                             Return x - y ; 
#                             Break;
#                         EndIf.    
#                     EndWhile.
#                 While c - a[5]
#                 EndDo.   
#             EndIf. 
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,68))
#     def test_69(self):
#         input = """Var: a[5] = {5,6,\"abc\"}, t = True, b = False ; 
#         Function: a
#         Parameter: f
#         Body:  
#             Var: param = {}; 
#             foo(\"abc\" && \"xyz\"); 
#             If running(root) Then a = 1; ElseIf e >=. 8 Then
#                 Do 
#                     While foo(\"neunhungayay\") Do 
#                         If (a + 0xFF) Then running(root); EndIf.
#                         Return a - 8; 
#                     EndWhile.
#                     If (a + 0xFF) Then running(root); EndIf.
#                     a = a[5]; 
#                     u (\"a\" && 8); 
#                     While c*8 
#                     Do 
#                         If (9 + 10e9) Then 
#                             running(root_left); 
#                             a = 10 - 8 ; 
#                             Return x - y ; 
#                         EndIf.    
#                     EndWhile.
#                 While c - a[5]
#                 EndDo.   
#             EndIf. 
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,69))
#     def test_70(self):
#         """Break khong dc nam trong If"""
#         input = """Var: a[5] = {5,6,\"abc\"}, t = True, b = False ; 
#         Function: a
#         Parameter: f
#         Body:  
#             Var: param = {}; 
#             foo(\"abc\" && \"xyz\"); 
#             If running(root) Then a = 1; ElseIf e >=. 8 Then
#                 Do 
#                     While foo(\"neunhungayay\") Do 
#                         If (a + 0xFF) Then running(root); EndIf.
#                         Return a - 8; 
#                     EndWhile.
#                     If (a + 0xFF) Then running(root); EndIf.
#                     a = a[5]; 
#                     u (\"a\" && 8); 
#                     Do 
#                         If (9 + 10e9) Then 
#                             running(root_left); 
#                             a = 10 - 8 ; 
#                             Return x - y ; 
#                         EndIf.    
#                     EndWhile.
#                 While c - a[5]
#                 EndDo.   
#             EndIf. 
#         EndBody.
#         """
#         expect = "Error on line 22 col 20: EndWhile"
#         self.assertTrue(TestParser.checkParser(input,expect,70))
#     def test_71(self):
#         """Break khong dc nam trong If"""
#         input = """Var: a, b = {5,6,"abc"}, m = 500; 
#         Function: tut
#         Parameter: ppl, ar[10]
#         Body:  
#             Var: param = 5; 
#             foo(!a); 
#             Return a - 2; 
#             arr[foo(a*2)][7+temp] = temp + 1; 
#             For (i = 5, n - i, i - 1) 
#             Do
#                 a = a - 1; 
#                 Break; 
#                 If e != \"E\" Then 
#                     r = \"R\"; 
#                     Return r;
#                 ElseIf e == \"E\" Then 
#                     d  = d;
#                     Return d; 
#                 Else d = \"D\"; 
#                 EndIf.
#                 Return foo(a[5]) ; 
#             EndFor.
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,71))
#     def test_72(self):
#         """"""
#         input = """Var: a, m = {5,6,7,{1,5}};
#         Function: pmain
#         Parameter: k, l, i
#         Body:  
#             Var: param = 5; 
#             If (6>5) Then a()[5] = 4; EndIf.
#             For (a = 8,i\.2,-i) Do
#                 a = a + 8 ; 
#                 h = h + k; 
#             EndFor. ** endForstm ** 
#             While  y && k
#             Do
#                 Do 
#                     a = 8; 
#                     y = y + t[5 - i -k];
#                 While y * 8
#                 EndDo.
#             EndWhile.
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,72))
#     def test_73(self):
#         """"""
#         input = """Var: a, m = {5,6,7,{1,5}};
#         Function: pmain
#         Parameter: k, l, i
#         Body:  
#             h = {1,2} + {5,8} ; 
#             foo("a",True, a[10]);
#             Return 8 + a[10][10];
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,73))
#     def test_74(self):
#         """Thieu ;"""
#         input = """Var: a, m = {5,6,7,{1,5}};
#         Function: pmain
#         Parameter: k, l, i
#         Body:  
#             h = {1,2} + {5,8} ; 
#             foo("a",True, a[10]);
#             If t > 8 * ar[5] Then **do nothing** EndIf.
#             For (i = 8, u + v, u *. v)
#             Do 
#                 Break; 
#                 Return r; 
#                 t = root_left
#                 root(root_right); 
#                 Do **do nothing**
#                 While -u 
#                 DoWhile.
#             Return 8 + a[10][10];
#         EndBody.
#         """
#         expect = "Error on line 13 col 16: root"
#         self.assertTrue(TestParser.checkParser(input,expect,74))
#     def test_75(self):
#         """Thieu ;"""
#         input = """Var: a, m = {5,6,7,{1,5}};
#         Function: pmain
#         Parameter: k, l, i
#         Body:  
#             h = {1,2} + {5,8} ; 
#             foo("a",True, a[10]);
#             If t > 8 * ar[5] Then **do nothing** EndIf.
#             For (i = 8, u + v, u *. v)
#             Do 
#                 Do
#                     Break; 
#                     Return r; 
#                     t = root_left;
#                     root(root_right); 
#                     While i + 8
#                     Do **do nothing**
#                     EndWhile.
#                     Break;
#                 While -u 
#                 EndDo.
#             EndFor.
#             Return 8 + a[10][10];
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,75))
#     def test_76(self):
#         input = """Var: a, m = {5,6,7,{1,5}};
#         Function: pmain
#         Parameter: k, l, i
#         Body:  
#             h = {1,2} + {5,8} ; 
#             foo("a",True, a[10]);
#             If t > 8 * ar[5] Then **do nothing** EndIf.
#             For (i = 8, u + v, u *. v)
#             Do 
#                 Do
#                     Break; 
#                     Return r; 
#                     While i + 8
#                     Do 
#                         a = -b + {True,False,8};
#                         a = a + 8; **add**
#                         Break; 
#                         Continue;
#                     EndWhile.
#                     Break;
#                 While -u 
#                 EndDo.
#             EndFor.
#             Return 8 + a[10][10];
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,76))
#     def test_77(self):
#         """"""
#         input = """Var: a, m = {5,6,7,{1,5}};
#         Function: pmain
#         Parameter: k, l, i
#         Body:  
#             h = {1,2} + {5,8} ; 
#             foo("a",True, a[10]);
#             If t > 8 * ar[5] Then **do nothing** EndIf.
#             For (i = 8, u + v, u *. v)
#             Do 
#                 Return a + "t"; 
#                 foo(i+1,k,a[10]); 
#             EndFor.
#             Return 8 + a[10][10];
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,77))
#     def test_78(self):
#         """Thieu ;"""
#         input = """Var: a, m = {5,6,7,{1,5}};
#         Function: pmain
#         Parameter: main, func, xuan_Mai; 
#         Body:  
#             h = {1,2} + {5,8} ; 
#             foo("a",True, a[10]);
#             If t > 8 * ar[5] Then **do nothing** EndIf.
#             For (i = 8, u + v, u *. v)
#             Do 
#                 Return a + "t"; 
#                 foo(i+1,k,a[10]); 
#             EndFor.
#             Return 8 + a[10][10];
#         EndBody.
#         """
#         expect = "Error on line 3 col 39: ;"
#         self.assertTrue(TestParser.checkParser(input,expect,78))
#     def test_79(self):
#         """Body k dc viet Hoa"""
#         input = """Var: a, m = {5,6,7,{1,5}};
#         Function: pmain
#         Parameter: main, func, xuan_Mai 
#         body:  
#             h = {1,2} + {5,8} ; 
#             foo("a",True, a[10]);
#             If t > 8 * ar[5] Then **do nothing** EndIf.
#             For (i = 8, u + v, u *. v)
#             Do 
#                 Return a + "t"; 
#                 foo(i+1,k,a[10]); 
#             EndFor.
#             Return 8 + a[10][10];
#         EndBody.
#         """
#         expect = "Error on line 4 col 8: body"
#         self.assertTrue(TestParser.checkParser(input,expect,79))
#     def test_80(self):
#         """"""
#         input = """Var: a, m = {5,6,7,{1,5}};
#         Function: pmain
#         Parameter: main, func, xuan_Mai 
#         Body:  
#             h = {1,2} + {5,8} ; 
#             foo("a",True, a[10]);
#             For (i = 8, u + v, u *. v)
#             Do 
#                 Return a + "t"; 
#                 foo(i+1,k,a[10]); 
#                 If t > 8 * ar[5] Then **do nothing** EndIf.
#                 For(i=1, -1, a[10])
#                 Do **nothing **
#                 EndFor.
#             EndFor.
#             Return a[10];
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,80))
#     def test_81(self):
#         """"""
#         input = """Var: a, m = {5,6,7,{1,5}};
#         Function: pmain
#         Parameter: main, func, xuan_Mai 
#         Body:  
#             h = {1,2} + {5,8} ; 
#             foo("a",True, a[10]);
#             For (i = 8, u + v, u *. v)
#             Do 
#                 Return a + "t"; 
#                 foo(i+1,k,a[10]); 
#                 If t > 8 * ar[5] Then **do nothing** EndIf.
#                 For(i=1, -1, a[10])
#                 Do 
#                     While i + (9*7)
#                     Do 
#                         Break;
#                         Continue; 
#                         a = -1; 
#                     EndWhile.
#                 EndFor.
#             EndFor.
#             Return a[10];
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,81))
#     def test_82(self):
#         """"""
#         input = """Var: a, m = {5,6,7,{1,5}};
#         Function: bkit
#         Parameter: main, func, xuan_Mai 
#         Body:  
#             h = {1,2} + foo(x,y,a[10]); 
#             For (i = 8, u + v, u *. v)
#             Do 
#                 Return a + "t"; **return_stm**
#                 foo(i+1,k,a[10]); 
#                 If t > 8 * ar[5] Then **do nothing** EndIf.
#                 For(i=1, -1, a[10]) **for_stm**
#                 Do 
#                     While i + (9*7)
#                     Do 
#                         Break; **Break_stm**
#                     EndWhile.
#                 EndFor.
#             EndFor.
#             Return a[10];
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,82))
#     def test_83(self):
#         """"""
#         input = """Var: a, m = {5,6,7,{1,5}};
#         Function: bkit
#         Parameter: main, func, xuan_Mai 
#         Body:  
#             h = {1,2} + foo(x,y,a[10]); 
#             For (i = 8, u + v, u *. v)
#             Do 
#                 Return a + "t"; **return_stm**
#                 foo(i+1,k,a[10]); 
#                 If t > 8 * ar[5] Then **do nothing** EndIf.
#                 For(i=1, -1, a[10]) **for_stm**
#                 Do 
#                     While i + (9*7)
#                     Do 
#                         Break; **Break_stm**
#                     EndWhile.
#                 EndFor.
#             EndFor.
#             Return a[10];
#         EndBody.
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,83))


