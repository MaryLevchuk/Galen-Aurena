timer    css    #timer

days    css    #days
days_number    css    #days_number
days_text    css    #days_text
hours    css    #hours
hours_number    css    #hours_number
hours_text    css    #hours_text
minutes    css    #minutes
minutes_number    css    #minutes_number
minutes_text    css    #minutes_text
=========================================================
timer
	contains: days, hours, minutes
	centered: screen

days
	contains: days_number, days_text
	near: hours left
hours
	contains: hours_number, hours_text
minutes
	contains: minutes_number, minutes_text
	near: hours right
