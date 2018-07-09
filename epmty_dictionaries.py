def fig_out_if_empty(Sample_list):
    isempty = True
    for dictionaries in Sample_list:
        if len(dictionaries) > 0:
            isempty = False
    if isempty == False:
        print "False"
    else:
        print "True"

Sample_list = [{},{},{}]
fig_out_if_empty(Sample_list)
