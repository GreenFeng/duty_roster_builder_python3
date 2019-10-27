import Window as win
import Worker

window = win.Windom()
group = Worker.Worker(window.NAME,[window.DAY,window.PERIOD])
print(group)