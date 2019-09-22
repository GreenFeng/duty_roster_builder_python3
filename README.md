# hellow-word
to make a duty roster manually is painful
but this program may help us to build a roster convenient

1.creat the worker class,the worker class request to:
  have date:
    string name: work's name
    bool worktime[7,5]: if workable in 7 days,6 periods
    bool state: if get more work
  have function:
    workable: return state
    set_worktime: chang worktime from False to True
    show_name: return name
    show_worktime: print worktime
