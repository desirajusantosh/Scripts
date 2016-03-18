set string_a "This is it"
if {[regexp -- {it$} $string_a]} {
  Puts "ends with 'it'"
}

if {![regexp -- {^HI} $string_a]} {
  Puts "does not begin with 'HI'"
}


set string_b "Call me at 007"
if {[regexp -- {(\d+)} $string_b -> number]} {
  Puts "contains number $number"
}

Puts [regsub -- { +at +} $string_b { later }]
