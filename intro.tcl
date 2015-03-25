#Basic TCL commands required for Synopsys PrimeTime 

#creating variable
set home_dir "/usr/home"

#passing environment variables(Unix and PrimeTime)
set home_dir $env(HOME)

#assigning input and outputs in design
all_input{input_1 input_2 input_3 clock sel}

all_output{output}

#help and man page
man set_false_path
set_false_path -help

#setting consrtaints on inputs and outputs
set_false_path -from [all_input] \ -to [all_output]

set_false_path -from [get_port input_1] \ -to [all_output]

#setting constraints using instance and pin names instead of nets
set_false_path -from [get_pin reg_heir/reg_1/Q] \ -to [get_pin reg_4/D]

set_false_path -from [get_pin reg_heir/reg_*/Q] \ -to [get_pin reg_4/*]
