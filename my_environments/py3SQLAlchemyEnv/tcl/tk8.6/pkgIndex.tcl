if {[catch {package present Tcl 8.6.0}]} { return }
if {($::tcl_platform(platform) eq "unix") && ([info exists ::env(DISPLAY)]
	|| ([info exists ::argv] && ("-display" in $::argv)))} {
<<<<<<< HEAD
    package ifneeded Tk 8.6.6 [list load [file join $dir .. .. bin libtk8.6.dll] Tk]
} else {
    package ifneeded Tk 8.6.6 [list load [file join $dir .. .. bin tk86tg.dll] Tk]
=======
    package ifneeded Tk 8.6.9 [list load [file join $dir .. .. bin libtk8.6.dll] Tk]
} else {
    package ifneeded Tk 8.6.9 [list load [file join $dir .. .. bin tk86t.dll] Tk]
>>>>>>> 311d4a7cb79f6cae733e750176059f554e8eaa98
}
