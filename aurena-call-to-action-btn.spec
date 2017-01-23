btn    css    #btn
btn_text css    #text
btn_icon css    #icon
========================================================
btn
	centered on the screen
	color: blue
	contains: btn_text
	
btn_text
	color: white
	
@@ if btn_text
		text contains: Play
@@ do
	btn_icon
		visible
	btn
		contains: btn_text, btn_icon
@@ end