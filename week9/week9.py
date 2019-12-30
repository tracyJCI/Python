def main ():
    nicks_street ={1 : ['adult_human','adult_human', 'cat','cat'],2: ['adult_humn','dog'], 3: ['adult_human','dog']}
# ddictionaries consist of (keys,values)

    print(nicks_street[2])

    nicks_street['peggys bucket'] = ['bucket','yeard']
    print(nicks_street['peggys bucket'])

    nicks_street['peggys bucket'].append('firepit')
    print (5 in nicks_street)




    import random
    count_dict = {}
    count_sum = 1
    top = 100
    step_count = 0

    all_step_counts =[]
    for i in range(10000):
        while count_sum<100:
            my_num = random.randint(0,11)
            count_sum+= my_num
            step_count +=1
        all_step_counts.append(step_count)

        #reset
        count_sum=0
        step_count=0
    count_dict={}
    for one_count in all_step_counts:
        if one_count in count_dict:
           count_dict[one_count] += 1
        else :
            count_dict[one_count]=1
    print(count_dict)


    total_steps = list(count_dict.keys())
    print(total_steps)
    print(total_steps.sort())
    print(total_steps)

    for one_step in total_steps:
        print(one_step,'appeared',count_dict[one_step],"times")

    def byFreq(pair):
        return pair[1]
    pair_list = count_dict.items()
    pair_list.sort(key=byFreq)
    print(pair_list)
    for pair in pair_list:
        print(pair[0],'appeared',pair[1],'times')

    from collections import Counter
    counts = dict(Counter(all_step_counts))
    print(counts)
main()
#import string
# for punc in string.puctuation:
     # print(punc)
