import sfml as sf

import static_shapes as stcp


def loadfile(rlist, filename):
    scene = open(filename, 'r')
    line_buff = scene.readline()
    for f in range(0, len(line_buff) - 1):
        if line_buff[0:6] == 'rectan':
            x = float(line_buff[6:12])
            y = float(line_buff[13:19])
            height = float(line_buff[20:26])
            wigth = float(line_buff[27:33])
            result_obj = stcp.Rectan()
            result_obj.position = sf.Vector2(x, y)
            result_obj.size = sf.Vector2(height, wigth)
            result_obj.fill_color = sf.Color.GREEN
            rlist.append(result_obj)
            #TODO: Make a color initialization
        elif line_buff[0:6] == 'circle':
            pass #TODO: Make a circle initialization
    return rlist
    scene.close()
