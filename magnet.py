import sfml as sf
import static_shapes as stsp
import init_obj

window = sf.RenderWindow(sf.VideoMode(640, 480), "magnetSim_py", sf.Style.TITLEBAR
| sf.Style.DEFAULT)
rectangle = stsp.MovingRect()
rectangle.position = sf.Vector2(10, 20)
rectangle.size = sf.Vector2(100, 500)
rectangle.outline_color = sf.Color.RED
rectangle.fill_color = sf.Color.CYAN
drawlist = []
drawlist = init_obj.loadfile(drawlist, 'scene.txt')
while window.is_open:
    for event in window.events:
        window.clear()
        for drawhat in range(0, len(drawlist)):
            drawlist[drawhat].rectupdate
            window.draw(drawlist[drawhat])
        window.display()
        if type(event) is sf.CloseEvent:
            window.close()