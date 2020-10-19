import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

        # TEST IDENTIFIER ......................................................................     
	def test_101(self):
		self.assertTrue(TestLexer.checkLexeme("DoanThanhNam1813130 **khung**", "Do,anThanhNam1813130,<EOF>", 101))
	def test_102(self):
		self.assertTrue(TestLexer.checkLexeme("Var", "Var,<EOF>", 102))
	def test_103(self):
		self.assertTrue(TestLexer.checkLexeme( "_a4", "Error Token _", 103))
	def test_104(self):
		self.assertTrue(TestLexer.checkLexeme( "Anhsangcuachanli", "Error Token A", 104))
	def test_105(self):
		self.assertTrue(TestLexer.checkLexeme( "thay_Phung_phong_do", "thay_Phung_phong_do,<EOF>", 105))
	def test_106(self):
		self.assertTrue(TestLexer.checkLexeme( "TA_1811442", "Error Token T", 106))
	def test_107(self):
		self.assertTrue(TestLexer.checkLexeme( "0o024", "0,o024,<EOF>", 107))
	def test_108(self):
		self.assertTrue(TestLexer.checkLexeme(" ", "<EOF>", 108))
	def test_110(self):
		self.assertTrue(TestLexer.checkLexeme("0a_3sd,abc", "0,a_3sd,,,abc,<EOF>", 110))
	def test_111(self):
		self.assertTrue(TestLexer.checkLexeme("-0xFF", "-,0xFF,<EOF>", 111))
	def test_112(self):
		self.assertTrue(TestLexer.checkLexeme( "4e4,0xFF,0XABC", "4e4,,,0xFF,,,0XABC,<EOF>", 112))
	def test_113(self):
		self.assertTrue(TestLexer.checkLexeme( "0.0e+00", "0.0e+00,<EOF>", 113))
	def test_114(self):
		self.assertTrue(TestLexer.checkLexeme( "0.0e+-", "0.0,e,+,-,<EOF>", 114))
	def test_115(self):
		self.assertTrue(TestLexer.checkLexeme( "0.o8", "0.,o8,<EOF>", 115))
	def test_116(self):
		self.assertTrue(TestLexer.checkLexeme( "0O7,0xABC", "0O7,,,0xABC,<EOF>", 116))
	def test_117(self):
		self.assertTrue(TestLexer.checkLexeme( "00e4,0.15e4", "0,0e4,,,0.15e4,<EOF>", 117)) 
	def test_118(self):
		self.assertTrue(TestLexer.checkLexeme( "0.8e-", "0.8,e,-,<EOF>", 118)) #phan e tru k co so
	def test_119(self):
		self.assertTrue(TestLexer.checkLexeme( "01.0000e4", "0,1.0000e4,<EOF>", 119)) #phan nguyen khong bat dau bang 0
	def test_120(self):
		self.assertTrue(TestLexer.checkLexeme( "0x", "0,x,<EOF>", 120)) 
	def test_121(self):
		self.assertTrue(TestLexer.checkLexeme( "1.0e0000", "1.0e0000,<EOF>", 121)) # so cuoi dc bang 0
	def test_122(self):
		self.assertTrue(TestLexer.checkLexeme( "TrueFalse", "True,False,<EOF>", 122))
	def test_123(self):
		self.assertTrue(TestLexer.checkLexeme( "DoWhile", "Do,While,<EOF>", 123))
	def test_124(self):
		self.assertTrue(TestLexer.checkLexeme( "Break; EndIf", "Break,;,EndIf,<EOF>", 124))
	def test_125(self):
		self.assertTrue(TestLexer.checkLexeme( "function, while", "function,,,while,<EOF>", 125))
	def test_126(self):
		self.assertTrue(TestLexer.checkLexeme( "Var 8", "Var,8,<EOF>", 126))
	def test_127(self):
		self.assertTrue(TestLexer.checkLexeme( "EndFor ENDWhile", "EndFor,Error Token E", 127))
	def test_128(self):
		self.assertTrue(TestLexer.checkLexeme( "a = True; b = False", "a,=,True,;,b,=,False,<EOF>", 128))
	def test_129(self):
		self.assertTrue(TestLexer.checkLexeme( "a = b + c + 10 ; ", "a,=,b,+,c,+,10,;,<EOF>", 129))
	def test_130(self):
		self.assertTrue(TestLexer.checkLexeme( "a = True_cf; b = False_fuse", "a,=,True,Error Token _", 130))
	def test_131(self):
		self.assertTrue(TestLexer.checkLexeme( "a == b \ c + 6", "a,==,b,\,c,+,6,<EOF>", 131))
	def test_132(self):
		self.assertTrue(TestLexer.checkLexeme("If ( a = 0 ) Do b = a;", "If,(,a,=,0,),Do,b,=,a,;,<EOF>", 132))
	def test_133(self):
		self.assertTrue(TestLexer.checkLexeme("FOR a = 5 DO a = a + 1", "Error Token F", 133))
	def test_134(self):
		self.assertTrue(TestLexer.checkLexeme("EndWhile ELse IF ENd", "EndWhile,Error Token E", 134))
	def test_135(self):
		self.assertTrue(TestLexer.checkLexeme("a = fALSE", "a,=,fALSE,<EOF>", 135))
	def test_136(self):
		self.assertTrue(TestLexer.checkLexeme("{ {}, {} } ","{ {}, {} },<EOF>",136))
	def test_137(self):
		self.assertTrue(TestLexer.checkLexeme("{ { \"a\" , 0.5 , 2 } , { 1 ,{ 11 , False , 13 } } }","{ { \"a\" , 0.5 , 2 } , { 1 ,{ 11 , False , 13 } } },<EOF>",137))
	def test_138(self):
		self.assertTrue(TestLexer.checkLexeme("{\"ab\"\"abc\n\"","{,ab,Unclosed String: abc\n",138))
	def test_139(self):
		self.assertTrue(TestLexer.checkLexeme("{{1,2,3}, {a,6,}}","{,{1,2,3},,,{,a,,,6,,,},},<EOF>",139))
	def test_140(self):
		self.assertTrue(TestLexer.checkLexeme("{{1,2,3},{4,5,6,{7,8,9}}}","{{1,2,3},{4,5,6,{7,8,9}}},<EOF>",140))
	def test_141(self):
		self.assertTrue(TestLexer.checkLexeme("{12e4,10.5}","{12e4,10.5},<EOF>",141))
	def test_142(self):
		self.assertTrue(TestLexer.checkLexeme("{True,False}","{True,False},<EOF>",142))
	def test_143(self):
		self.assertTrue(TestLexer.checkLexeme("{-0x7F,0,2}","{,-,0x7F,,,0,,,2,},<EOF>",143))
	def test_144(self):
		self.assertTrue(TestLexer.checkLexeme("{\"Phan Le Tuan Anh\",{\"1811442\",\"PPL\"}, {\"HK1\"}}","{\"Phan Le Tuan Anh\",{\"1811442\",\"PPL\"}, {\"HK1\"}},<EOF>",144))
	def test_145(self):
		self.assertTrue(TestLexer.checkLexeme( "** khai *bao bien ** Var: a,b = 2,5,6 ; Parameter: Body:  x = 10; funcn(a);  EndBody. ", "Var,:,a,,,b,=,2,,,5,,,6,;,Parameter,:,Body,:,x,=,10,;,funcn,(,a,),;,EndBody,.,<EOF>",145))
	def test_146(self):
		self.assertTrue(TestLexer.checkLexeme("If root == NULL then root = newPtr; taller = true; return root; EndIf. ","If,root,==,Error Token N",146))
	def test_147(self):
		self.assertTrue(TestLexer.checkLexeme("inOrder(root_left); process(root); inOrder(root_right); EndIf.","inOrder,(,root_left,),;,process,(,root,),;,inOrder,(,root_right,),;,EndIf,.,<EOF>",147))
	def test_148(self):
		self.assertTrue(TestLexer.checkLexeme("If i % 2 == 0 **biendem** Then write(i); dem:=dem+1;EndFor.If dem = 15 Then dem:=0;writeln(dem);","If,i,%,2,==,0,Then,write,(,i,),;,dem,:,=,dem,+,1,;,EndFor,.,If,dem,=,15,Then,dem,:,=,0,;,writeln,(,dem,),;,<EOF>",148))
	def test_149(self):
		self.assertTrue(TestLexer.checkLexeme(" Body: If a>b Then tg=a; a=b;  b=g;  EndIf. EndBody.", "Body,:,If,a,>,b,Then,tg,=,a,;,a,=,b,;,b,=,g,;,EndIf,.,EndBody,.,<EOF>", 149))
	def test_150(self):
		self.assertTrue(TestLexer.checkLexeme("Parameter: a,b FUction: main", "Parameter,:,a,,,b,Error Token F", 150))
	def test_151(self):
		self.assertTrue(TestLexer.checkLexeme("Var a = 5; **khai bao ,b", "Var,a,=,5,;,Unterminated Comment", 151))  #mo ma khong dong cmt
	def test_152(self):
		self.assertTrue(TestLexer.checkLexeme("a**ifidf**,f5", "a,,,f5,<EOF>", 152))
	def test_153(self):
		self.assertTrue(TestLexer.checkLexeme("\"**ifidf**\",f5", "**ifidf**,,,f5,<EOF>", 153)) 
	def test_155(self):
		self.assertTrue(TestLexer.checkLexeme("{{\"dog **smartdog**\", **Supercat** \"cat\",\"Peguin\" **best Peguin},{\"height\",\"weight\",{\"4.5\",\"8.7\"}}}","{,{,dog **smartdog**,,,cat,,,Peguin,Unterminated Comment", 155)) 
	def test_156(self):
		self.assertTrue(TestLexer.checkLexeme("*one\n*two\n*three\n*","*,one,*,two,*,three,*,<EOF>",156))
	def test_157(self):
		self.assertTrue(TestLexer.checkLexeme("*one\\n*two\\n*three\\n*","*,one,\,n,*,two,\,n,*,three,\,n,*,<EOF>",157))
	def test_158(self):
		self.assertTrue(TestLexer.checkLexeme("*****", "*,<EOF>", 158))
	def test_159(self):
		self.assertTrue(TestLexer.checkLexeme(" \"15  09 //2020\", 15 + 9 = 24, arr[5] = {7,8,9}, ELSEIF", "15  09 //2020,,,15,+,9,=,24,,,arr,[,5,],=,{7,8,9},,,Error Token E", 159))
	def test_160(self):
		self.assertTrue(TestLexer.checkLexeme("a = 7 ;","a,=,7,;,<EOF>", 160))
	def test_161(self):
		self.assertTrue(TestLexer.checkLexeme("\\****\';:","\,Error Token '", 161))
	def test_162(self):
		self.assertTrue(TestLexer.checkLexeme("   a = 8, Var, DoWhile;","a,=,8,,,Var,,,Do,While,;,<EOF>", 162))
	def test_163(self):
		self.assertTrue(TestLexer.checkLexeme("\"True\", arr = {1 , 5, 8, ***, EOF}","True,,,arr,=,{,1,,,5,,,8,,,Unterminated Comment", 163))
	def test_164(self):
		self.assertTrue(TestLexer.checkLexeme("\"True\", arr = {1 , 5, 8, **av**, eOF}","True,,,arr,=,{,1,,,5,,,8,,,,,eOF,},<EOF>", 164))
	def test_165(self):
		self.assertTrue(TestLexer.checkLexeme(" \"abc**f**\"","abc**f**,<EOF>", 165)) 
	def test_166(self):
		self.assertTrue(TestLexer.checkLexeme("\"True\"","True,<EOF>", 166))
	def test_167(self):
		self.assertTrue(TestLexer.checkLexeme(" \"Neu nhu \\n ngay ay \" ", "Neu nhu \\n ngay ay ,<EOF>", 167))
	def test_168(self):
		self.assertTrue(TestLexer.checkLexeme(" \"Neu nhu \\\n ngay ay \" ", "Illegal Escape In String: Neu nhu \\\n", 168))
	def test_169(self):
		self.assertTrue(TestLexer.checkLexeme(" \"Anh se tot ma \\g ngay ay \" ", "Illegal Escape In String: Anh se tot ma \\g", 169))
	def test_170(self):
		self.assertTrue(TestLexer.checkLexeme(" \"Anh se tot ma \\\g ngay ay \" ", "Anh se tot ma \\\\g ngay ay ,<EOF>", 170))
	def test_171(self):
		self.assertTrue(TestLexer.checkLexeme(" \"Anh se tot ma \\\\g ngay ay \" ", "Anh se tot ma \\\\g ngay ay ,<EOF>", 171))
	def test_172(self):
		self.assertTrue(TestLexer.checkLexeme(" \"Neu nhu \t ngay ay \" ", "Neu nhu 	 ngay ay ,<EOF>", 172))
	def test_173(self):
		self.assertTrue(TestLexer.checkLexeme("\"\\n\"","\\n,<EOF>",173))
	def test_174(self):
		self.assertTrue(TestLexer.checkLexeme("\"abc,5,2\n\"","Unclosed String: abc,5,2\n",174))
	def test_175(self):
		self.assertTrue(TestLexer.checkLexeme("\"\\\\n\"","\\\\n,<EOF>",175)) 
	def test_176(self):
		self.assertTrue(TestLexer.checkLexeme("\"Phan Le Tuan Anh \\t 1811442\"","Phan Le Tuan Anh \\t 1811442,<EOF>",176))
	def test_177(self):
		self.assertTrue(TestLexer.checkLexeme("","<EOF>",177))
	def test_178(self):
		self.assertTrue(TestLexer.checkLexeme("\"Var int a \\t \\n = 8\"","Var int a \\t \\n = 8,<EOF>", 178))
	def test_179(self):
		self.assertTrue(TestLexer.checkLexeme("\"Phan Le Tuan Anh \\\\t 1811442\"","Phan Le Tuan Anh \\\\t 1811442,<EOF>",179))
	def test_180(self):
		self.assertTrue(TestLexer.checkLexeme(" \"string\"abc\"","string,abc,Unclosed String: ", 180))
	def test_181(self):
		self.assertTrue(TestLexer.checkLexeme("\"abc\\\\r def\"","abc\\\\r def,<EOF>",181))
	def test_182(self):
		self.assertTrue(TestLexer.checkLexeme("\"abc \\r def\"","abc \\r def,<EOF>",182))
	def test_183(self):
		self.assertTrue(TestLexer.checkLexeme("\"abc \\a def\"","Illegal Escape In String: abc \\a",183))
	def test_184(self):
		self.assertTrue(TestLexer.checkLexeme("\"Phan Le\\n TA","Unclosed String: Phan Le\\n TA",184))
	def test_185(self):
		self.assertTrue(TestLexer.checkLexeme("\"Phan Le \\k TA\"","Illegal Escape In String: Phan Le \k",185))
	def test_186(self):
		self.assertTrue(TestLexer.checkLexeme("\"Phan Le \f  xyz\"","Phan Le   xyz,<EOF>",186))
	def test_187(self):
		self.assertTrue(TestLexer.checkLexeme("\"Phan Le \\f  xyz\"","Phan Le \\f  xyz,<EOF>",187))
	def test_188(self):
		self.assertTrue(TestLexer.checkLexeme("\"Phan Le \' xyz\"","Illegal Escape In String: Phan Le ' ",188))
	def test_189(self):
		self.assertTrue(TestLexer.checkLexeme("\"Phan Le \\a xyz\"","Illegal Escape In String: Phan Le \\a",189)) #???????????????????????//
	def test_190(self):
		self.assertTrue(TestLexer.checkLexeme("arr[0][8] = {{** \"If th**en  else**\"  **,5,8},{0.1e8,0O78},{0xABC,2}}}", "arr,[,0,],[,8,],=,{,{,en,else,,,5,,,8,},,,{,0.1e8,,,0O7,8,},,,{0xABC,2},},},<EOF>", 190)) 
	def test_191(self):
		self.assertTrue(TestLexer.checkLexeme("{1,2,**a**,3}", "{,1,,,2,,,,,3,},<EOF>", 191)) 
	def test_192(self):
		self.assertTrue(TestLexer.checkLexeme("\"a,b **a**bc\"", "a,b **a**bc,<EOF>", 192)) 
	def test_193(self):
		self.assertTrue(TestLexer.checkLexeme("\"He asked me:  \'\"Where is John\'\"\"","He asked me:  \'\"Where is John\'\",<EOF>", 193))
	def test_194(self):
		self.assertTrue(TestLexer.checkLexeme("\"abc \\r def\"","abc \\r def,<EOF>",194))
	def test_195(self):
		self.assertTrue(TestLexer.checkLexeme("\"abc \\a def\"","Illegal Escape In String: abc \\a",195))
	def test_196(self):
		self.assertTrue(TestLexer.checkLexeme(" \"this is a string:\'\"abc\nxyz\"", "Unclosed String: this is a string:\'\"abc\n", 196))
	def test_197(self):
		input = """\"abc
		xyz\""""
		self.assertTrue(TestLexer.checkLexeme(input,"Unclosed String: abc\n",197)) 
	def test_198(self):
		input = """\"abc \\ xyz\""""
		self.assertTrue(TestLexer.checkLexeme(input,"Illegal Escape In String: abc \\ ",198)) 
	def test_199(self):
		input = """\"abc \\xyz\""""
		self.assertTrue(TestLexer.checkLexeme(input,"Illegal Escape In String: abc \\x",199))
	def test_200(self):
		input = """\"abc \\\\ xyz\""""
		self.assertTrue(TestLexer.checkLexeme(input,"abc \\\\ xyz,<EOF>",200))
	def test_201(self):
		input = """\"\\\z\""""
		self.assertTrue(TestLexer.checkLexeme(input,"\\\\z,<EOF>",201))
    
# import unittest
# from TestUtils import TestLexer

# class LexerSuite(unittest.TestCase):
#     def test_lower_identifier(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>", 100))

#     def test_lower_upper_id(self):
#         self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>", 101))

#     def test_wrong_token(self):
#         self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?", 102))

#     def test_integer(self):
#         """test integers"""
#         self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>", 103))

#     def test_illegal_escape(self):
#         """test illegal escape"""
#         self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""", 104))

#     def test_unterminated_string(self):
#         """test unclosed string"""
#         self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """, 105))

#     def test_normal_string_with_escape(self):
#         """test normal string with escape"""
#         self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""", 106))
#     def test_unterminated_comment(self):
#         input ="""
#         ** This is a
#         * multi-line
#         * comment
#         **"""
#         self.assertTrue(TestLexer.checkLexeme(input, "<EOF>", 107))
#     def test_case_9(self):
#         input = """
#         "this is a string'"\k"
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """Illegal Escape In String: this is a string'"\k""", 108))
#     def test_case_10(self):
#         input = "0o0423"
#         self.assertTrue(TestLexer.checkLexeme(input, "0,o0423,<EOF>", 109))
#     def test_case_11(self):
#         input = "Ask"
#         self.assertTrue(TestLexer.checkLexeme(input, "Error Token A", 110))
#     def test_case_12(self):
#         input = "Var: x = 12e-5;";
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,12e-5,;,<EOF>", 111))
#     def test_case_13(self):
#         input = "Var: a = {1,2,43;";
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,a,=,{,1,,,2,,,43,;,<EOF>", 112))
#     def test_case_14(self):
#         input = "a[3 + foo(2)] = a[b[2][3]] + 4;"
#         self.assertTrue(TestLexer.checkLexeme(input, "a,[,3,+,foo,(,2,),],=,a,[,b,[,2,],[,3,],],+,4,;,<EOF>", 113))
#     def test_case_15(self):
#         input = "**this a commen(*$^*%&#^&**"
#         self.assertTrue(TestLexer.checkLexeme(input, "<EOF>", 114))
#     def test_case_16(self):
#         input = "**this is a comment*&^52465"
#         self.assertTrue(TestLexer.checkLexeme(input, "Unterminated Comment", 115))
#     def test_case_17(self):
#         input = "**just a comment*(&^%&*"
#         self.assertTrue(TestLexer.checkLexeme(input, "Unterminated Comment", 116))
#     def test_case_18(self):
#         input = """
#         Function: main
#         Body:
#             x = 10;
#             fact(x);
#         EndBody.
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Function,:,main,Body,:,x,=,10,;,fact,(,x,),;,EndBody,.,<EOF>", 117))
#     def test_case_19(self):
#         input = """ "string \\\ string\\' hjg" """
#         self.assertTrue(TestLexer.checkLexeme(input, "string \\\ string\\' hjg,<EOF>", 118))
#     def test_case_20(self):
#         input = "v = (4. \. 3.) *. 3.14 *. r *. r *. r;"
#         self.assertTrue(TestLexer.checkLexeme(input, "v,=,(,4.,\.,3.,),*.,3.14,*.,r,*.,r,*.,r,;,<EOF>", 119))
#     def test_case_21(self):
#         input = """
#         "hjagfysugd'"afsdg'"agd"
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """hjagfysugd'"afsdg'"agd,<EOF>""", 120))
#     def test_case_22(self):
#         input = """
#         "fklasjghs'"assgf'\""""
#         self.assertTrue(TestLexer.checkLexeme(input, """Unclosed String: fklasjghs'"assgf'\"""", 121))
#     def test_case_23(self):
#         input = "Var x:$;"
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,x,:,Error Token $", 122))
#     def test_case_24(self):
#         input = "0_dAaf"
#         self.assertTrue(TestLexer.checkLexeme(input, "0,Error Token _", 123))
#     def test_case_25(self):
#         input = """
#         Var: a = 1, b[10], s = "ajkg'", dA;"""
#         self.assertTrue(TestLexer.checkLexeme(input, """Var,:,a,=,1,,,b,[,10,],,,s,=,Unclosed String: ajkg'", dA;""", 124))
#     def test_case_26(self):
#         input = """
#         Function: fact
#         Parameter: n
#         Body:
#             If n == 0 Then
#                 Return 1;
#             Else
#                 Return n * fact (n - 1);
#             EndIf.
#         EndBody."""
#         self.assertTrue(TestLexer.checkLexeme(input, "Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,<EOF>", 125))
#     def test_case_27(self):
#         input = """
#         Function: foo
#         Parameter: a[5], b
#         Body:
#             Var: i = 0;
#             While (i < 5)
#                 a[i] = b +. 1.0;
#                 i += 1;
#             EndWhile.
#         EndBody."""
#         self.assertTrue(TestLexer.checkLexeme(input, "Function,:,foo,Parameter,:,a,[,5,],,,b,Body,:,Var,:,i,=,0,;,While,(,i,<,5,),a,[,i,],=,b,+.,1.0,;,i,+,=,1,;,EndWhile,.,EndBody,.,<EOF>", 126))
#     def test_case_28(self):
#         input = "Var: b[2][3]={{1,2,3},{4,5,6}};"
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,b,[,2,],[,3,],=,{,{,1,,,2,,,3,},,,{,4,,,5,,,6,},},;,<EOF>", 127))
#     def test_case_29(self):
#         input = "*lkaf**"
#         self.assertTrue(TestLexer.checkLexeme(input, "*,lkaf,Unterminated Comment", 128))
#     def test_case_30(self):
#         input = "foo (2 + x, 4. \. y);"
#         self.assertTrue(TestLexer.checkLexeme(input, "foo,(,2,+,x,,,4.,\.,y,),;,<EOF>", 129))
#     def test_case_31(self):
#         input = """
#             If (True)
#                 s = 0o248542;
#             EndIf."""
#         self.assertTrue(TestLexer.checkLexeme(input, "If,(,True,),s,=,0o24,8542,;,EndIf,.,<EOF>", 130))
#     def test_case_32(self):
#         input = """
#         If (True || False)
#             print("aff\g\d");
#         EndIf.
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "If,(,True,||,False,),print,(,Illegal Escape In String: aff\g", 131))
#     def test_case_33(self):
#         input = "Var# x = 12;"
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,Error Token #", 132))
#     def test_case_34(self):
#         input = "Var: x; x =/= 10;"
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,;,x,=/=,10,;,<EOF>", 133))
#     def test_case_35(self):
#         input = """
#         Var: x = "124\\f\\b98";
#         Var: y = "1234"""
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,124\\f\\b98,;,Var,:,y,=,Unclosed String: 1234", 134))
#     def test_case_36(self):
#         input = """
#         Var: a = "kagfus\\a\\k\\o";"""
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,a,=,Illegal Escape In String: kagfus\\a", 135))
#     def test_case_37(self):
#         input ="""**kjgsjgh*jhs\\f"""
#         self.assertTrue(TestLexer.checkLexeme(input, """Unterminated Comment""", 136))
#     def test_case_38(self):
#         input ="""
#         "asd\\uf"**comm\\n\\kent**"""
#         self.assertTrue(TestLexer.checkLexeme(input, """Illegal Escape In String: asd\\u""", 137))
#     def test_case_39(self):
#         input ="""
#         **comm\\n\\kent**"""
#         self.assertTrue(TestLexer.checkLexeme(input, "<EOF>", 138))
#     def test_case_40(self):
#         input = "0xFF0o0843"
#         self.assertTrue(TestLexer.checkLexeme(input, "0xFF0,o0843,<EOF>", 139))
#     def test_case_41(self):
#         input = """
#         Var: x = 10;
#         ** define
#         * variable
#         *
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,10,;,Unterminated Comment", 140))
#     def test_case_42(self):
#         input = """
#         Var: x = 10.e2;
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,10.e2,;,<EOF>", 141))
#     def test_case_43(self):
#         input = """
#         Var: flag = False;
#         flag = !flag;
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,flag,=,False,;,flag,=,!,flag,;,<EOF>", 142))
#     def test_case_44(self):
#         input = """
#         Var: x = 10.e2;
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,10.e2,;,<EOF>", 143))
#     def test_case_45(self):
#         input = """
#         Var: x = 'asdaf';
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,Error Token '", 144))
#     def test_case_46(self):
#         input = """
#         "\\bkkg\\fh\\tdsf\\n'"fsd'"f\\r\\\gdshg\\'"
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """\\bkkg\\fh\\tdsf\\n'"fsd'"f\\r\\\gdshg\\',<EOF>""", 145))
#     def test_case_47(self):
#         input = """
#         Var: f = -10e+;
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,f,=,-,10,e,+,;,<EOF>", 146))
#     def test_case_48(self):
#         input = """
#         x_kaf124kah_ = (1 < 2) && (2. < 3.);
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "x_kaf124kah_,=,(,1,<,2,),&&,(,2.,<,3.,),;,<EOF>", 147))
#     def test_case_49(self):
#         input = """Var: variable-@list;"""
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,variable,-,Error Token @", 148))
#     def test_case_50(self):
#         input = """
#         s = "dajfsg;"""
#         self.assertTrue(TestLexer.checkLexeme(input, "s,=,Unclosed String: dajfsg;", 149))
#     def test_case_51(self):
#         input = """ "dahgsfgs\\'fg'" kasdj\\t gi \\bda's" """
#         self.assertTrue(TestLexer.checkLexeme(input, """Illegal Escape In String: dahgsfgs\\'fg'" kasdj\\t gi \\bda's""", 150))
#     def test_case_52(self):
#         input = """
#         ** "How How \\a \\b \\c
#         * \\e '
#         **
#         Var: 09 = {;
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,0,9,=,{,;,<EOF>", 151))
#     def test_case_53(self):
#         input = """
#         If (9 == 1 == 2 > 4)
#             Var: vv;
#         EndIf.
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "If,(,9,==,1,==,2,>,4,),Var,:,vv,;,EndIf,.,<EOF>", 152))
#     def test_case_54(self):
#         input = """
#         v = v && 1 || !(v - 1);
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "v,=,v,&&,1,||,!,(,v,-,1,),;,<EOF>", 153))
#     def test_case_55(self):
#         input = """
#         v = v && 1 || !(v - 1);
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "v,=,v,&&,1,||,!,(,v,-,1,),;,<EOF>", 154))
#     def test_case_56(self):
#         input = """
#         Var: X[10] = 1;
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,Error Token X", 155))
#     def test_case_57(self):
#         input = """
#         print("hjf
#         it's me")
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "print,(,Unclosed String: hjf\n", 156))
#     def test_case_58(self):
#         input = """
#         print(**hjf
#         it's me** "veo veo")
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "print,(,veo veo,),<EOF>", 157))
#     def test_case_59(self):
#         input = """
#         0x_Fjsjsj * 0kdk;
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "0,x_Fjsjsj,*,0,kdk,;,<EOF>", 158))
#     def test_case_60(self):
#         input = """
#         "'"'"\\'\\f\\b~!@#$%^&/?|*('"
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """Unclosed String: '"'"\\'\\f\\b~!@#$%^&/?|*('\"\n""", 159))
#     def test_case_61(self):
#         input = """
#         print(**hjf
#         #     it's me* "veo veo")
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "print,(,Unterminated Comment", 160))
#     def test_case_62(self):
#         input = """
#         Function: fact
#         Parameter: n
#         Body:
#             foo(2 + a[0][1 + 2 * 3 - 4 * n]) = 2 + f("ssss");
#         EndBody.
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Function,:,fact,Parameter,:,n,Body,:,foo,(,2,+,a,[,0,],[,1,+,2,*,3,-,4,*,n,],),=,2,+,f,(,ssss,),;,EndBody,.,<EOF>", 161))
#     def test_case_63(self):
#         input = """
#         If (a_ == 0214)
#             *a = a % 6 + 2 != 4 + kikk \. 24;
#         EndIf.
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "If,(,a_,==,0,214,),*,a,=,a,%,6,+,2,!=,4,+,kikk,\.,24,;,EndIf,.,<EOF>", 162))
#     def test_case_64(self):
#         input = """
#         "Illegal Escape In String''error
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Illegal Escape In String: Illegal Escape In String''", 163))
#     def test_case_65(self):
#         input = """
#         For( i = 0, i < 100, i += 2)
#             i = i ** i;
#         EndFor.
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "For,(,i,=,0,,,i,<,100,,,i,+,=,2,),i,=,i,Unterminated Comment", 164))
#     def test_case_66(self):
#         input = """
#         Var: i = 0;
#         While (i < 20)
#             print(string_of_int(i *. 10));
#             ** this is a comment **
#             x = int_of_string(get_str());
#         EndWhile.
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,i,=,0,;,While,(,i,<,20,),print,(,string_of_int,(,i,*.,10,),),;,x,=,int_of_string,(,get_str,(,),),;,EndWhile,.,<EOF>", 165))
#     def test_case_67(self):
#         input = """
#         Var: x = 123.e+++-+123;
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,123.,e,+,+,+,-,+,123,;,<EOF>", 166))
#     def test_case_68(self):
#         input = """
#         Var: x = 172.17.31.62;
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,172.17,.,31.62,;,<EOF>", 167))
#     def test_case_69(self):
#         input = """
#         Var: x = e++ - 12.e;
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,e,+,+,-,12.,e,;,<EOF>", 168))
#     def test_case_70(self):
#         input = """
#         Var: x = 2 ^ 4 + 4 * 102 + 1 << 10;
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,2,Error Token ^", 169))
#     def test_case_71(self):
#         input = """
#         "asdfghjklqwertyui\\b\\\\\\wop zxcvbnm"
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """Illegal Escape In String: asdfghjklqwertyui\\b\\\\\\w""", 170))
#     def test_case_72(self):
#         input = """
#         Var: x = new int[10];
#         Do
#         *(x + i) = i *. 2 -. 10;
#         While i < 10 EndDo.
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """Var,:,x,=,new,int,[,10,],;,Do,*,(,x,+,i,),=,i,*.,2,-.,10,;,While,i,<,10,EndDo,.,<EOF>""", 171))
#     def test_case_73(self):
#         input = """
#         * line line **
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """*,line,line,Unterminated Comment""", 172))
#     def test_case_74(self):
#         input = """
#         "'"* line line **"
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """'"* line line **,<EOF>""", 173))
#     def test_case_75(self):
#         input = """
#         Var: flag = False;
#         If flag
#             a[2 , 1, 2, :] = a[:].mean(axis = 0)
#         EndIf.
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,flag,=,False,;,If,flag,a,[,2,,,1,,,2,,,:,],=,a,[,:,],.,mean,(,axis,=,0,),EndIf,.,<EOF>", 174))
#     def test_case_76(self):
#         input = """
#         Var: a = {1 { 2        { 3{4{    "         "}}  }}};
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Var,:,a,=,{,1,{,2,{,3,{,4,{,         ,},},},},},;,<EOF>", 175))
#     def test_case_77(self):
#         input = """
#         foo(3 + 4. \\. 1.24e+-2 + a[2. =/= 5.][g(1)]);
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "foo,(,3,+,4.,\.,1.24,e,+,-,2,+,a,[,2.,=/=,5.,],[,g,(,1,),],),;,<EOF>", 176))
#     def test_case_78(self):
#         input = """
#         **\\a " ** "A01290435" False .234;
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "A01290435,False,.,234,;,<EOF>", 177))
#     def test_case_79(self):
#         input = """
#        "String string bla blu lalalulu\\'s  '"daf'"'" \\b \\n \\f \\r \\t bing bing"
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """String string bla blu lalalulu\\'s  '"daf'"'" \\b \\n \\f \\r \\t bing bing,<EOF>""", 178))
#     def test_case_80(self):
#         input = """
#         dasd - asd * 213 (False && true)"____"{bdb, jdas, 1 +. e2, 1. \\. 2e2}
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "dasd,-,asd,*,213,(,False,&&,true,),____,{,bdb,,,jdas,,,1,+.,e2,,,1.,\.,2e2,},<EOF>", 179))
#     def test_case_81(self):
#         input = """
#         Function: main
#         'docs'
#         Body:
#         EndBody.
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Function,:,main,Error Token '", 180))
#     def test_case_82(self):
#         input = """
#         Function: main
#         'docs'
#         Body:
#         EndBody.
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Function,:,main,Error Token '", 181))
#     def test_case_83(self):
#         input = """
#        ***iajsfdsg*sjkghsfg***
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "*,<EOF>", 182))
#     def test_case_84(self):
#         input = """
#        ***iajsfdsg*sjkghsfg**
#        "jaja\\'\\'\\'";
#        "'"asdaf'"";
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """jaja\\'\\'\\',;,'"asdaf'",;,<EOF>""", 183))
#     def test_case_85(self):
#         input = """
#         Var: x = "dasd"; {123, 123, **dahg***}[12 "ads"] = 5%6 \.132 -.-.-.;
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """Var,:,x,=,dasd,;,{,123,,,123,,,*,},[,12,ads,],=,5,%,6,\.,132,-.,-.,-.,;,<EOF>""", 184))
#     def test_case_86(self):
#         input = """
#         While x = 1: pass.{}[123][f(12, "dasf" +. 123 +. +. *. 123)];
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """While,x,=,1,:,pass,.,{,},[,123,],[,f,(,12,,,dasf,+.,123,+.,+.,*.,123,),],;,<EOF>""", 185))
#     def test_case_87(self):
#         input = """
#         For (i = 0, i < 17, i ** i) Do
#             print(print(i(i)));
#         EndFor.
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """For,(,i,=,0,,,i,<,17,,,i,Unterminated Comment""", 186))
#     def test_case_88(self):
#         input = """
#         Function: dka34
#         x = 31230o0123;
#         Var: x = f((123));
#         EndFor.
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """Function,:,dka34,x,=,31230,o0123,;,Var,:,x,=,f,(,(,123,),),;,EndFor,.,<EOF>""", 187))
#     def test_case_89(self):
#         input = """
#             If (if == 123):
#                 x = "dasfgf'" 123\\' \\b\\f \\\\"
#             x = [123];
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """If,(,if,==,123,),:,x,=,dasfgf'" 123\\' \\b\\f \\\\,x,=,[,123,],;,<EOF>""", 188))
#     def test_case_90(self):
#         input = """
#             x = "\\\' \\b\\f \\\\ fshg'%"
#             x = [123];
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """x,=,Illegal Escape In String: \\' \\b\\f \\\\ fshg'%""", 189))
#     def test_case_91(self):
#         input = """
#             x = {12, "32"13, &23, 1243, ""};
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """x,=,{,12,,,32,13,,,Error Token &""", 190))
#     def test_case_92(self):
#         input = """
#             x = ...--.-.-----.+.++++.;
#             x = *.*.*.*.*. \\.\\.\\.;
#             x = "124{34}" ***324**;
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """x,=,.,.,.,-,-.,-.,-,-,-,-,-.,+.,+,+,+,+.,;,x,=,*.,*.,*.,*.,*.,\.,\.,\.,;,x,=,124{34},;,<EOF>""", 191))
#     def test_case_93(self):
#         input = """
#             x[True, False, 1 : 10, :newaxis] = {True, False};
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """x,[,True,,,False,,,1,:,10,,,:,newaxis,],=,{,True,,,False,},;,<EOF>""", 192))
#     def test_case_94(self):
#         input = """
#             x = {blue, b**3***, 2 * 3, 2. *. 43[34] + 13 -. 2}["asd'"'"'"'"];
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """x,=,{,blue,,,b,*,,,2,*,3,,,2.,*.,43,[,34,],+,13,-.,2,},[,Unclosed String: asd'"'"'"'"];\n""", 193))
#     def test_case_95(self):
#         input = """
#             x = 0124 * 41350x012432 + 0x123134 + 123. 4234 && 123.asdsg || (14(f()));
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """x,=,0,124,*,41350,x012432,+,0x123134,+,123.,4234,&&,123.,asdsg,||,(,14,(,f,(,),),),;,<EOF>""", 194))
#     def test_case_96(self):
#         input = """
#             x = {     **dasd*** ***1324j***   123    } + 12394X013 + 132;
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """x,=,{,*,*,123,},+,12394,Error Token X""", 195))
#     def test_case_97(self):
#         input = """
#             x = "das\\t\\b\\'\\t\\n\\r\\r\\nf" + 13.123O12314;"""
#         self.assertTrue(TestLexer.checkLexeme(input, """x,=,das\\t\\b\\'\\t\\n\\r\\r\\nf,+,13.123,Error Token O""", 196))
#     def test_case_98(self):
#         input = """
#             x = 123 + 123.adfgg + {123, {{{{"daf"}}}}};
#             x = || 1&& ;
#             x =/= 9 != 10 >. 123 <=. aaa;"""
#         self.assertTrue(TestLexer.checkLexeme(input, """x,=,123,+,123.,adfgg,+,{,123,,,{,{,{,{,daf,},},},},},;,x,=,||,1,&&,;,x,=/=,9,!=,10,>.,123,<=.,aaa,;,<EOF>""", 197))
#     def test_case_99(self):
#         input = """
#             If False Then
#             ElseIf Then
#             Then
#             print("dasd\\\\'"\\1");
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """If,False,Then,ElseIf,Then,Then,print,(,Illegal Escape In String: dasd\\\\'"\\1""", 198))
#     def test_case_100(self):
#         input = """
#             ** this ***
#             blue = th * th -. 1230x423ar235ljfg && 4234 || e13;
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, """*,blue,=,th,*,th,-.,1230,x423ar235ljfg,&&,4234,||,e13,;,<EOF>""", 199))
#     def test_case_101(self):
#         input = """
#         ** **
#         Function: main
#         Body:
#             Var: x = {{{1,  2 ,2e-124, "avc" , -1 }, {  4 , **erty**  5}  },  {{ 6  ,  7  },{ 8,9}}};
#         EndBody.
#         ** **
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Function,:,main,Body,:,Var,:,x,=,{,{,{,1,,,2,,,2e-124,,,avc,,,-,1,},,,{,4,,,5,},},,,{,{,6,,,7,},,,{,8,,,9,},},},;,EndBody,.,<EOF>", 200))
#     def test_case_102(self):
#         input = """
#         x = .123, 03124.4234, 0.+e123, 123.e, 123.123e-1123;
#         123.e+, 1.e13, 1.e-123, 213e
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "x,=,.,123,,,03124.4234,,,0.,+,e123,,,123.,e,,,123.123e-1123,;,123.,e,+,,,1.e13,,,1.e-123,,,213,e,<EOF>", 201))
#     def test_case_103(self):
#         input = """
#         "asdasd
#         jkhgsd"
#         """
#         self.assertTrue(TestLexer.checkLexeme(input, "Unclosed String: asdasd\n", 202))
#     def test_case_104(self):
#         self.assertTrue(TestLexer.checkLexeme(""" " che6.7ck \\\\\\ d\t \n wow \\ m rek" """, """Illegal Escape In String:  che6.7ck \\\\\\ """, 203))
#     def test_case_105(self):
#         self.assertTrue(TestLexer.checkLexeme("0000.0 03123 000 312.000e1123 3123e140000", """0000.0,0,3123,0,0,0,312.000e1123,3123e140000,<EOF>""", 204))


	


