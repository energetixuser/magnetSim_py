import sfml as sf

import static_shapes as stcp


def loadfile(rlist, filename):
    scene = open(filename, 'r')
    line_buff = scene.readline()
    for f in range(0, len(line_buff) - 1):
        if line_buff[0:3] == 'rect':
            x = float(scene.read(5))
            y = float(scene.read(5))
            scene.read(1)
            height = float(scene.read(5))
            wigth = float(scene.read(5))
            ch_buff = scene.read(1)
            result_obj = stcp.MovingRect()
            result_obj.position = sf.Vector2(x, y)
            result_obj.size = sf.Vector2(height, wigth)
            result_obj.fill_color = sf.Color.GREEN
            rlist.append(result_obj)
            if ch_buff != '\n': #TODO: Make a color initialization
                pass
        elif line_buff[0:3] == 'circ':
            pass
    return rlist
    scene.close()
