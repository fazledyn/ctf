from Cryptodome.Util.number import inverse

n = 61669858299163074006210163971633827955468705486215421096918483050987641223200830111435902516663559308368041654398047033295910537091953317837076480672140808272694579713291914230438195477363700383883666497368142369778983233316761131312116273094256003580628371454778356307820672516228661024247237853915924534853

e1 = 10335920110133746448747119203906685637728747851909050368596147216733493272777562131343630694349445721664276816716626957343685474358712679266952789613103343
d1 = 5423221742370115779039332084915302134217252787500419654351430271329601982428475155853209992288119248844642695321666574363723729709887492230423215797280744056613846673931164848178023950808900046984719376204098265884223263307000819948404884126373233433012325706159625727870087117048839645853419288822281132351

e2 = 7800339247142052676358650555898178528588229490593656068002716362799261418896737076128731974674874475137149596620517126758184540483455881098419648873379601

c = 57169125809270801921716028957776162725276734684705960556047638447652661296922371755224496932800131286797562226965382257865366713599122195614647728997716079119349907533333163728931843674914172461742183199194926816848467881576845921284185108314783944498503671661640561524112459532158818663751586209332795906975

# phi = (p-1)*(q-1)
# d = inverse(E, phi)
# m = pow(C, d, N)

phi = d1 * e1 - 1
d2 = inverse(e2, phi)
m = pow(c, d2, n)

hex_val = hex(m)[2:]
print(hex_val)
ascii_val = bytes.fromhex(hex_val).decode("utf-8")
print(ascii_val)