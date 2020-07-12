import numpy as np

HORSE_EXPECTED = np.array(
    [
        [9, 350],
        [10, 350],
        [11, 350],
        [12, 350],
        [13, 350],
        [14, 349],
        [15, 349],
        [16, 349],
        [17, 349],
        [18, 349],
        [19, 350],
        [18, 351],
        [17, 352],
        [16, 353],
        [15, 353],
        [14, 354],
        [13, 355],
        [12, 355],
        [11, 356],
        [10, 357],
        [9, 357],
        [9, 358],
        [10, 358],
        [11, 358],
        [12, 358],
        [13, 358],
        [14, 358],
        [15, 357],
        [16, 357],
        [17, 357],
        [18, 357],
        [19, 357],
        [20, 356],
        [21, 356],
        [22, 355],
        [23, 355],
        [24, 354],
        [25, 355],
        [26, 355],
        [27, 356],
        [28, 357],
        [29, 358],
        [30, 359],
        [31, 360],
        [32, 361],
        [33, 362],
        [34, 363],
        [35, 364],
        [36, 365],
        [37, 365],
        [38, 366],
        [39, 366],
        [40, 367],
        [41, 367],
        [42, 367],
        [43, 367],
        [44, 368],
        [45, 368],
        [46, 368],
        [47, 369],
        [48, 369],
        [49, 369],
        [50, 370],
        [51, 370],
        [52, 370],
        [53, 371],
        [54, 371],
        [55, 372],
        [56, 372],
        [57, 373],
        [58, 373],
        [59, 374],
        [60, 374],
        [61, 375],
        [62, 375],
        [63, 376],
        [64, 376],
        [65, 377],
        [66, 377],
        [67, 378],
        [68, 378],
        [69, 379],
        [70, 380],
        [71, 380],
        [72, 381],
        [73, 381],
        [74, 382],
        [75, 382],
        [76, 383],
        [77, 384],
        [78, 384],
        [79, 385],
        [80, 385],
        [81, 386],
        [82, 387],
        [83, 387],
        [84, 388],
        [85, 388],
        [86, 388],
        [87, 388],
        [88, 388],
        [89, 387],
        [90, 387],
        [91, 386],
        [92, 386],
        [93, 385],
        [94, 384],
        [95, 383],
        [96, 383],
        [97, 382],
        [98, 382],
        [99, 381],
        [100, 380],
        [100, 379],
        [100, 378],
        [100, 377],
        [100, 376],
        [100, 375],
        [100, 374],
        [100, 373],
        [101, 372],
        [101, 371],
        [102, 370],
        [101, 369],
        [101, 368],
        [100, 367],
        [99, 367],
        [98, 366],
        [97, 366],
        [96, 365],
        [95, 365],
        [94, 364],
        [93, 364],
        [92, 363],
        [91, 363],
        [90, 362],
        [89, 361],
        [88, 360],
        [87, 360],
        [86, 359],
        [85, 358],
        [84, 357],
        [84, 356],
        [83, 355],
        [82, 354],
        [81, 353],
        [80, 352],
        [80, 351],
        [79, 350],
        [79, 349],
        [78, 348],
        [78, 347],
        [77, 346],
        [77, 345],
        [77, 344],
        [76, 343],
        [76, 342],
        [76, 341],
        [75, 340],
        [75, 339],
        [75, 338],
        [74, 337],
        [74, 336],
        [73, 335],
        [73, 334],
        [73, 333],
        [72, 332],
        [72, 331],
        [72, 330],
        [71, 329],
        [71, 328],
        [70, 327],
        [71, 326],
        [72, 326],
        [73, 325],
        [74, 325],
        [75, 324],
        [76, 324],
        [77, 324],
        [78, 323],
        [79, 323],
        [80, 323],
        [81, 322],
        [82, 322],
        [83, 322],
        [84, 321],
        [85, 321],
        [86, 321],
        [87, 321],
        [88, 320],
        [89, 320],
        [90, 320],
        [91, 319],
        [92, 319],
        [93, 319],
        [94, 319],
        [95, 318],
        [96, 318],
        [97, 318],
        [98, 318],
        [99, 317],
        [100, 317],
        [101, 317],
        [102, 317],
        [103, 316],
        [104, 316],
        [105, 316],
        [106, 316],
        [107, 316],
        [108, 315],
        [109, 315],
        [110, 315],
        [111, 315],
        [112, 314],
        [113, 314],
        [114, 314],
        [115, 313],
        [116, 313],
        [117, 312],
        [118, 312],
        [119, 311],
        [120, 311],
        [121, 311],
        [122, 310],
        [123, 310],
        [124, 309],
        [125, 309],
        [126, 309],
        [127, 309],
        [128, 309],
        [129, 309],
        [130, 308],
        [131, 308],
        [132, 308],
        [133, 308],
        [134, 308],
        [135, 308],
        [136, 308],
        [137, 308],
        [138, 308],
        [139, 308],
        [140, 308],
        [141, 307],
        [142, 307],
        [143, 307],
        [144, 307],
        [145, 307],
        [146, 307],
        [147, 307],
        [148, 307],
        [149, 307],
        [150, 307],
        [151, 307],
        [152, 306],
        [153, 306],
        [154, 306],
        [155, 306],
        [156, 306],
        [157, 306],
        [158, 306],
        [159, 306],
        [160, 305],
        [161, 305],
        [162, 305],
        [163, 305],
        [164, 305],
        [165, 305],
        [166, 304],
        [167, 304],
        [168, 304],
        [169, 304],
        [170, 303],
        [171, 303],
        [172, 303],
        [173, 302],
        [174, 301],
        [175, 301],
        [176, 300],
        [177, 299],
        [178, 299],
        [179, 298],
        [180, 297],
        [181, 296],
        [182, 295],
        [183, 294],
        [184, 293],
        [185, 293],
        [186, 292],
        [187, 292],
        [188, 292],
        [189, 292],
        [190, 291],
        [191, 291],
        [192, 291],
        [193, 291],
        [194, 290],
        [195, 290],
        [196, 290],
        [197, 289],
        [198, 289],
        [199, 289],
        [200, 289],
        [201, 288],
        [202, 288],
        [203, 288],
        [204, 287],
        [205, 287],
        [206, 287],
        [207, 286],
        [208, 286],
        [209, 286],
        [210, 286],
        [211, 285],
        [212, 285],
        [213, 285],
        [214, 284],
        [215, 284],
        [216, 284],
        [217, 283],
        [218, 283],
        [219, 283],
        [220, 282],
        [221, 282],
        [222, 282],
        [223, 281],
        [224, 281],
        [225, 281],
        [226, 281],
        [227, 280],
        [228, 280],
        [229, 280],
        [230, 280],
        [231, 280],
        [232, 280],
        [233, 279],
        [234, 279],
        [235, 279],
        [236, 279],
        [237, 279],
        [238, 279],
        [239, 279],
        [240, 278],
        [241, 278],
        [242, 278],
        [243, 278],
        [244, 277],
        [245, 277],
        [246, 277],
        [247, 277],
        [248, 277],
        [249, 276],
        [250, 276],
        [251, 276],
        [252, 275],
        [253, 275],
        [254, 275],
        [255, 275],
        [256, 274],
        [257, 274],
        [258, 274],
        [259, 273],
        [260, 273],
        [261, 273],
        [262, 273],
        [263, 273],
        [264, 272],
        [265, 272],
        [266, 272],
        [267, 272],
        [268, 272],
        [269, 272],
        [270, 272],
        [271, 272],
        [272, 272],
        [273, 272],
        [274, 271],
        [275, 271],
        [276, 271],
        [277, 271],
        [278, 272],
        [279, 272],
        [280, 272],
        [281, 272],
        [282, 272],
        [283, 272],
        [284, 272],
        [285, 272],
        [286, 272],
        [287, 273],
        [288, 273],
        [289, 273],
        [290, 274],
        [291, 274],
        [292, 274],
        [293, 275],
        [294, 275],
        [295, 276],
        [296, 277],
        [297, 278],
        [298, 279],
        [299, 280],
        [300, 281],
        [301, 282],
        [301, 283],
        [302, 284],
        [303, 285],
        [304, 286],
        [305, 287],
        [305, 288],
        [306, 289],
        [307, 290],
        [308, 290],
        [309, 291],
        [310, 290],
        [311, 290],
        [311, 289],
        [311, 288],
        [312, 287],
        [312, 286],
        [312, 285],
        [312, 284],
        [312, 283],
        [312, 282],
        [312, 281],
        [312, 280],
        [312, 279],
        [312, 278],
        [312, 277],
        [312, 276],
        [312, 275],
        [312, 274],
        [311, 273],
        [310, 272],
        [309, 272],
        [308, 272],
        [307, 271],
        [306, 271],
        [305, 271],
        [304, 271],
        [303, 270],
        [302, 270],
        [301, 270],
        [300, 269],
        [299, 268],
        [298, 267],
        [297, 266],
        [296, 266],
        [295, 266],
        [294, 266],
        [293, 266],
        [292, 266],
        [291, 265],
        [290, 265],
        [289, 265],
        [288, 265],
        [287, 265],
        [286, 265],
        [285, 265],
        [284, 265],
        [283, 265],
        [282, 265],
        [281, 265],
        [280, 265],
        [279, 265],
        [278, 265],
        [277, 265],
        [276, 265],
        [275, 265],
        [274, 264],
        [273, 264],
        [272, 264],
        [271, 264],
        [270, 264],
        [269, 264],
        [268, 264],
        [267, 264],
        [266, 264],
        [265, 264],
        [264, 264],
        [263, 264],
        [262, 264],
        [261, 264],
        [260, 264],
        [259, 264],
        [258, 264],
        [257, 264],
        [256, 263],
        [255, 263],
        [254, 263],
        [253, 263],
        [252, 263],
        [251, 263],
        [250, 263],
        [249, 263],
        [248, 262],
        [249, 261],
        [250, 260],
        [251, 260],
        [252, 259],
        [253, 259],
        [254, 259],
        [255, 258],
        [256, 258],
        [257, 258],
        [258, 258],
        [259, 257],
        [260, 257],
        [261, 257],
        [262, 257],
        [263, 256],
        [264, 256],
        [265, 256],
        [266, 256],
        [267, 256],
        [268, 256],
        [269, 256],
        [270, 256],
        [271, 256],
        [272, 256],
        [273, 256],
        [274, 256],
        [275, 256],
        [276, 256],
        [277, 256],
        [278, 256],
        [279, 256],
        [280, 256],
        [281, 256],
        [282, 256],
        [283, 256],
        [284, 256],
        [285, 256],
        [286, 256],
        [287, 256],
        [288, 256],
        [289, 256],
        [290, 257],
        [291, 257],
        [292, 257],
        [293, 258],
        [294, 258],
        [295, 259],
        [296, 259],
        [297, 260],
        [298, 261],
        [299, 262],
        [300, 263],
        [301, 264],
        [302, 265],
        [303, 266],
        [304, 266],
        [305, 267],
        [306, 268],
        [307, 268],
        [307, 267],
        [308, 266],
        [308, 265],
        [308, 264],
        [308, 263],
        [308, 262],
        [309, 261],
        [309, 260],
        [309, 259],
        [309, 258],
        [309, 257],
        [309, 256],
        [309, 255],
        [309, 254],
        [309, 253],
        [309, 252],
        [308, 251],
        [307, 250],
        [306, 250],
        [305, 250],
        [304, 250],
        [303, 250],
        [302, 250],
        [301, 249],
        [300, 249],
        [299, 249],
        [298, 249],
        [297, 248],
        [296, 247],
        [295, 246],
        [294, 245],
        [293, 245],
        [292, 245],
        [291, 245],
        [290, 245],
        [289, 245],
        [288, 245],
        [287, 245],
        [286, 245],
        [285, 245],
        [284, 245],
        [283, 245],
        [282, 245],
        [281, 245],
        [280, 245],
        [279, 246],
        [278, 246],
        [277, 246],
        [276, 246],
        [275, 246],
        [274, 246],
        [273, 246],
        [272, 246],
        [271, 246],
        [270, 247],
        [269, 247],
        [268, 247],
        [267, 247],
        [266, 247],
        [265, 247],
        [264, 247],
        [263, 247],
        [262, 247],
        [261, 248],
        [260, 248],
        [259, 248],
        [258, 248],
        [257, 248],
        [256, 248],
        [255, 248],
        [254, 248],
        [253, 248],
        [252, 248],
        [251, 248],
        [250, 248],
        [249, 249],
        [248, 249],
        [247, 249],
        [246, 249],
        [245, 249],
        [244, 249],
        [243, 249],
        [242, 249],
        [241, 249],
        [240, 249],
        [239, 249],
        [238, 249],
        [237, 249],
        [236, 249],
        [235, 250],
        [234, 250],
        [233, 250],
        [232, 250],
        [231, 250],
        [230, 250],
        [229, 250],
        [228, 250],
        [227, 250],
        [226, 250],
        [225, 250],
        [224, 250],
        [223, 250],
        [222, 250],
        [221, 250],
        [220, 250],
        [219, 250],
        [218, 250],
        [217, 250],
        [216, 250],
        [215, 250],
        [214, 250],
        [213, 250],
        [212, 251],
        [211, 251],
        [210, 251],
        [209, 250],
        [208, 250],
        [207, 250],
        [206, 250],
        [205, 250],
        [204, 250],
        [203, 250],
        [202, 250],
        [201, 250],
        [200, 250],
        [199, 250],
        [198, 250],
        [197, 250],
        [196, 250],
        [195, 250],
        [194, 250],
        [193, 250],
        [192, 250],
        [191, 250],
        [190, 250],
        [189, 249],
        [188, 248],
        [188, 247],
        [188, 246],
        [188, 245],
        [188, 244],
        [188, 243],
        [188, 242],
        [188, 241],
        [188, 240],
        [188, 239],
        [188, 238],
        [187, 237],
        [187, 236],
        [187, 235],
        [187, 234],
        [187, 233],
        [187, 232],
        [187, 231],
        [187, 230],
        [187, 229],
        [187, 228],
        [187, 227],
        [187, 226],
        [187, 225],
        [187, 224],
        [187, 223],
        [187, 222],
        [187, 221],
        [187, 220],
        [187, 219],
        [187, 218],
        [187, 217],
        [187, 216],
        [186, 215],
        [186, 214],
        [186, 213],
        [186, 212],
        [186, 211],
        [186, 210],
        [186, 209],
        [186, 208],
        [186, 207],
        [186, 206],
        [186, 205],
        [186, 204],
        [186, 203],
        [186, 202],
        [186, 201],
        [186, 200],
        [186, 199],
        [186, 198],
        [185, 197],
        [185, 196],
        [185, 195],
        [185, 194],
        [185, 193],
        [185, 192],
        [185, 191],
        [185, 190],
        [185, 189],
        [185, 188],
        [185, 187],
        [184, 186],
        [184, 185],
        [184, 184],
        [184, 183],
        [184, 182],
        [184, 181],
        [183, 180],
        [183, 179],
        [183, 178],
        [183, 177],
        [183, 176],
        [182, 175],
        [182, 174],
        [182, 173],
        [182, 172],
        [181, 171],
        [181, 170],
        [181, 169],
        [180, 168],
        [180, 167],
        [180, 166],
        [179, 165],
        [179, 164],
        [179, 163],
        [178, 162],
        [178, 161],
        [177, 160],
        [177, 159],
        [176, 158],
        [176, 157],
        [175, 156],
        [175, 155],
        [174, 154],
        [174, 153],
        [173, 152],
        [173, 151],
        [172, 150],
        [172, 149],
        [171, 148],
        [171, 147],
        [170, 146],
        [170, 145],
        [169, 144],
        [169, 143],
        [168, 142],
        [168, 141],
        [168, 140],
        [167, 139],
        [167, 138],
        [167, 137],
        [167, 136],
        [166, 135],
        [167, 134],
        [167, 133],
        [168, 132],
        [169, 131],
        [170, 130],
        [171, 129],
        [172, 128],
        [173, 128],
        [174, 127],
        [175, 127],
        [176, 126],
        [177, 125],
        [178, 125],
        [179, 125],
        [180, 124],
        [181, 124],
        [182, 123],
        [183, 123],
        [184, 122],
        [185, 122],
        [186, 121],
        [187, 121],
        [188, 121],
        [189, 120],
        [190, 120],
        [191, 119],
        [192, 119],
        [193, 119],
        [194, 118],
        [195, 118],
        [196, 118],
        [197, 117],
        [198, 117],
        [199, 117],
        [200, 116],
        [201, 116],
        [202, 116],
        [203, 115],
        [204, 115],
        [205, 115],
        [206, 114],
        [207, 114],
        [208, 114],
        [209, 113],
        [210, 113],
        [211, 113],
        [212, 113],
        [213, 112],
        [214, 112],
        [215, 112],
        [216, 112],
        [217, 112],
        [218, 111],
        [219, 111],
        [220, 111],
        [221, 111],
        [222, 111],
        [223, 110],
        [224, 110],
        [225, 110],
        [226, 110],
        [227, 110],
        [228, 110],
        [229, 109],
        [230, 109],
        [231, 109],
        [232, 109],
        [233, 109],
        [234, 109],
        [235, 109],
        [236, 108],
        [237, 108],
        [238, 108],
        [239, 108],
        [240, 108],
        [241, 108],
        [242, 108],
        [243, 108],
        [244, 108],
        [245, 108],
        [246, 108],
        [247, 108],
        [248, 108],
        [249, 108],
        [250, 108],
        [251, 108],
        [252, 108],
        [253, 108],
        [254, 108],
        [255, 108],
        [256, 108],
        [257, 108],
        [258, 108],
        [259, 109],
        [260, 109],
        [261, 109],
        [262, 110],
        [263, 110],
        [264, 110],
        [265, 111],
        [266, 111],
        [267, 111],
        [268, 112],
        [269, 112],
        [270, 112],
        [271, 113],
        [272, 113],
        [273, 114],
        [274, 114],
        [275, 114],
        [276, 115],
        [277, 115],
        [278, 116],
        [279, 116],
        [280, 116],
        [281, 117],
        [282, 117],
        [283, 118],
        [284, 118],
        [285, 119],
        [286, 120],
        [287, 121],
        [288, 122],
        [289, 123],
        [290, 124],
        [291, 125],
        [292, 126],
        [293, 127],
        [294, 128],
        [295, 129],
        [296, 130],
        [297, 130],
        [298, 131],
        [299, 132],
        [300, 133],
        [301, 133],
        [302, 132],
        [303, 131],
        [304, 130],
        [304, 129],
        [304, 128],
        [304, 127],
        [304, 126],
        [304, 125],
        [304, 124],
        [304, 123],
        [304, 122],
        [304, 121],
        [303, 120],
        [303, 119],
        [303, 118],
        [302, 117],
        [301, 116],
        [300, 115],
        [299, 115],
        [298, 115],
        [297, 114],
        [296, 114],
        [295, 114],
        [294, 113],
        [293, 113],
        [292, 112],
        [291, 112],
        [290, 111],
        [289, 110],
        [288, 109],
        [288, 108],
        [287, 107],
        [286, 106],
        [285, 105],
        [284, 104],
        [283, 104],
        [282, 104],
        [281, 104],
        [280, 103],
        [279, 103],
        [278, 103],
        [277, 103],
        [276, 103],
        [275, 102],
        [274, 102],
        [273, 102],
        [272, 102],
        [271, 102],
        [270, 102],
        [269, 101],
        [268, 101],
        [267, 101],
        [266, 101],
        [265, 101],
        [264, 101],
        [263, 101],
        [262, 100],
        [261, 100],
        [260, 100],
        [259, 100],
        [258, 100],
        [257, 100],
        [256, 100],
        [255, 100],
        [254, 99],
        [253, 99],
        [252, 99],
        [251, 99],
        [250, 99],
        [249, 99],
        [248, 99],
        [247, 98],
        [246, 98],
        [245, 98],
        [244, 98],
        [243, 98],
        [242, 97],
        [241, 97],
        [240, 97],
        [239, 96],
        [238, 96],
        [237, 95],
        [236, 95],
        [235, 94],
        [234, 94],
        [233, 93],
        [232, 93],
        [231, 92],
        [230, 92],
        [229, 91],
        [228, 91],
        [227, 90],
        [226, 90],
        [225, 90],
        [224, 89],
        [223, 89],
        [222, 89],
        [221, 89],
        [220, 89],
        [219, 89],
        [218, 89],
        [217, 89],
        [216, 89],
        [215, 90],
        [214, 90],
        [213, 90],
        [212, 90],
        [211, 91],
        [210, 91],
        [209, 91],
        [208, 91],
        [207, 92],
        [206, 92],
        [205, 92],
        [204, 91],
        [204, 90],
        [205, 89],
        [206, 88],
        [206, 87],
        [207, 86],
        [208, 85],
        [209, 84],
        [210, 83],
        [211, 82],
        [212, 81],
        [213, 80],
        [214, 79],
        [215, 78],
        [216, 78],
        [217, 77],
        [218, 76],
        [219, 75],
        [220, 74],
        [221, 74],
        [222, 73],
        [223, 72],
        [224, 72],
        [225, 71],
        [226, 70],
        [227, 70],
        [228, 69],
        [229, 68],
        [230, 68],
        [231, 67],
        [232, 67],
        [233, 66],
        [234, 66],
        [235, 65],
        [236, 65],
        [237, 64],
        [238, 64],
        [239, 63],
        [240, 63],
        [241, 62],
        [242, 62],
        [243, 62],
        [244, 61],
        [245, 61],
        [246, 60],
        [247, 60],
        [248, 60],
        [249, 60],
        [250, 59],
        [251, 59],
        [252, 59],
        [253, 59],
        [254, 58],
        [255, 58],
        [256, 58],
        [257, 58],
        [258, 58],
        [259, 58],
        [260, 58],
        [261, 58],
        [262, 58],
        [263, 58],
        [264, 57],
        [265, 57],
        [266, 57],
        [267, 57],
        [268, 57],
        [269, 57],
        [270, 57],
        [271, 57],
        [272, 57],
        [273, 57],
        [274, 57],
        [275, 57],
        [276, 57],
        [277, 57],
        [278, 57],
        [279, 57],
        [280, 57],
        [281, 57],
        [282, 57],
        [283, 57],
        [284, 57],
        [285, 57],
        [286, 58],
        [287, 58],
        [288, 58],
        [289, 59],
        [290, 60],
        [291, 61],
        [292, 62],
        [293, 63],
        [294, 64],
        [295, 65],
        [296, 66],
        [297, 67],
        [298, 68],
        [299, 68],
        [300, 69],
        [301, 70],
        [302, 70],
        [303, 71],
        [304, 72],
        [305, 72],
        [306, 73],
        [307, 73],
        [308, 73],
        [309, 73],
        [310, 72],
        [310, 71],
        [310, 70],
        [310, 69],
        [310, 68],
        [311, 67],
        [311, 66],
        [311, 65],
        [311, 64],
        [311, 63],
        [310, 62],
        [310, 61],
        [310, 60],
        [310, 59],
        [309, 58],
        [309, 57],
        [308, 56],
        [307, 55],
        [306, 54],
        [305, 53],
        [304, 52],
        [303, 52],
        [302, 52],
        [301, 52],
        [300, 52],
        [299, 52],
        [298, 52],
        [297, 52],
        [296, 52],
        [295, 52],
        [294, 51],
        [294, 50],
        [293, 49],
        [293, 48],
        [293, 47],
        [292, 46],
        [292, 45],
        [291, 44],
        [290, 44],
        [289, 44],
        [288, 44],
        [287, 44],
        [286, 44],
        [285, 45],
        [284, 45],
        [283, 45],
        [282, 45],
        [281, 45],
        [280, 46],
        [279, 46],
        [278, 46],
        [277, 46],
        [276, 47],
        [275, 47],
        [274, 47],
        [273, 47],
        [272, 48],
        [271, 48],
        [270, 48],
        [269, 48],
        [268, 48],
        [267, 49],
        [266, 49],
        [265, 49],
        [264, 49],
        [263, 49],
        [262, 49],
        [261, 49],
        [260, 49],
        [259, 49],
        [258, 49],
        [257, 49],
        [256, 49],
        [255, 49],
        [254, 49],
        [253, 49],
        [252, 49],
        [251, 49],
        [250, 49],
        [249, 49],
        [248, 49],
        [247, 49],
        [246, 49],
        [245, 49],
        [244, 49],
        [243, 49],
        [242, 49],
        [241, 49],
        [240, 49],
        [239, 49],
        [238, 49],
        [237, 49],
        [236, 49],
        [235, 50],
        [234, 50],
        [233, 50],
        [232, 50],
        [231, 50],
        [230, 50],
        [229, 50],
        [228, 50],
        [227, 50],
        [226, 50],
        [225, 50],
        [224, 50],
        [223, 50],
        [222, 50],
        [221, 50],
        [220, 50],
        [219, 51],
        [218, 51],
        [217, 52],
        [216, 53],
        [215, 53],
        [214, 54],
        [213, 55],
        [212, 56],
        [211, 57],
        [210, 58],
        [209, 58],
        [208, 59],
        [207, 60],
        [206, 61],
        [205, 61],
        [204, 62],
        [203, 63],
        [202, 63],
        [201, 64],
        [200, 64],
        [199, 65],
        [198, 65],
        [197, 66],
        [196, 66],
        [195, 66],
        [194, 67],
        [193, 67],
        [192, 67],
        [191, 67],
        [190, 68],
        [189, 68],
        [188, 68],
        [187, 68],
        [186, 68],
        [185, 68],
        [184, 68],
        [183, 68],
        [182, 67],
        [181, 67],
        [180, 67],
        [179, 67],
        [178, 67],
        [177, 66],
        [176, 66],
        [175, 66],
        [174, 65],
        [173, 65],
        [172, 65],
        [171, 65],
        [170, 64],
        [169, 64],
        [168, 64],
        [167, 63],
        [166, 63],
        [165, 63],
        [164, 62],
        [163, 62],
        [162, 62],
        [161, 61],
        [160, 61],
        [159, 61],
        [158, 60],
        [157, 60],
        [156, 60],
        [155, 59],
        [154, 59],
        [153, 59],
        [152, 59],
        [151, 58],
        [150, 58],
        [149, 58],
        [148, 57],
        [147, 57],
        [146, 57],
        [145, 57],
        [144, 57],
        [143, 56],
        [142, 56],
        [141, 56],
        [140, 56],
        [139, 56],
        [138, 56],
        [137, 56],
        [136, 56],
        [135, 56],
        [134, 55],
        [133, 55],
        [132, 55],
        [131, 55],
        [130, 55],
        [129, 55],
        [128, 55],
        [127, 55],
        [126, 55],
        [125, 55],
        [124, 56],
        [123, 56],
        [122, 56],
        [121, 56],
        [120, 56],
        [119, 56],
        [118, 57],
        [117, 57],
        [116, 58],
        [115, 58],
        [114, 58],
        [113, 59],
        [112, 59],
        [111, 60],
        [110, 60],
        [109, 61],
        [108, 61],
        [107, 62],
        [106, 63],
        [105, 63],
        [104, 64],
        [103, 64],
        [102, 64],
        [101, 64],
        [100, 63],
        [100, 62],
        [100, 61],
        [101, 60],
        [102, 59],
        [103, 59],
        [104, 58],
        [105, 57],
        [106, 57],
        [107, 56],
        [108, 56],
        [109, 56],
        [110, 55],
        [111, 55],
        [112, 54],
        [113, 54],
        [114, 54],
        [115, 53],
        [116, 53],
        [117, 53],
        [118, 52],
        [119, 52],
        [120, 52],
        [121, 52],
        [122, 51],
        [123, 51],
        [124, 51],
        [125, 51],
        [126, 51],
        [127, 51],
        [128, 51],
        [129, 51],
        [130, 51],
        [131, 51],
        [132, 51],
        [133, 51],
        [134, 50],
        [135, 50],
        [136, 50],
        [137, 50],
        [138, 50],
        [139, 50],
        [140, 50],
        [141, 50],
        [142, 50],
        [143, 50],
        [144, 50],
        [145, 50],
        [146, 50],
        [147, 50],
        [148, 50],
        [149, 50],
        [150, 50],
        [151, 50],
        [152, 50],
        [153, 50],
        [154, 50],
        [155, 50],
        [156, 50],
        [157, 50],
        [158, 50],
        [159, 50],
        [160, 50],
        [161, 50],
        [162, 50],
        [163, 50],
        [164, 50],
        [165, 50],
        [166, 50],
        [167, 50],
        [168, 50],
        [169, 50],
        [170, 50],
        [171, 50],
        [172, 50],
        [173, 50],
        [174, 50],
        [175, 50],
        [176, 50],
        [177, 50],
        [178, 50],
        [179, 50],
        [180, 49],
        [181, 49],
        [182, 49],
        [183, 49],
        [184, 49],
        [185, 49],
        [186, 49],
        [187, 49],
        [188, 49],
        [189, 49],
        [190, 49],
        [191, 49],
        [192, 49],
        [193, 49],
        [194, 49],
        [195, 49],
        [196, 49],
        [197, 49],
        [198, 49],
        [199, 49],
        [200, 49],
        [201, 49],
        [202, 49],
        [203, 49],
        [204, 49],
        [205, 49],
        [206, 48],
        [207, 48],
        [208, 48],
        [209, 48],
        [210, 48],
        [211, 47],
        [212, 47],
        [213, 47],
        [214, 46],
        [215, 46],
        [216, 46],
        [217, 46],
        [218, 45],
        [219, 45],
        [220, 45],
        [221, 45],
        [222, 45],
        [223, 44],
        [224, 44],
        [225, 44],
        [226, 44],
        [227, 43],
        [228, 43],
        [229, 43],
        [230, 43],
        [231, 42],
        [232, 42],
        [233, 42],
        [234, 42],
        [235, 41],
        [236, 41],
        [237, 41],
        [238, 41],
        [239, 40],
        [240, 40],
        [241, 40],
        [242, 39],
        [243, 39],
        [244, 39],
        [245, 38],
        [246, 37],
        [247, 36],
        [248, 35],
        [247, 35],
        [246, 35],
        [245, 34],
        [246, 33],
        [247, 33],
        [248, 33],
        [249, 33],
        [250, 33],
        [251, 32],
        [251, 31],
        [251, 30],
        [250, 30],
        [249, 29],
        [248, 29],
        [247, 29],
        [246, 29],
        [245, 28],
        [244, 28],
        [243, 28],
        [242, 28],
        [241, 28],
        [240, 28],
        [239, 28],
        [238, 27],
        [239, 26],
        [240, 26],
        [241, 26],
        [242, 26],
        [243, 25],
        [244, 25],
        [245, 25],
        [244, 24],
        [243, 24],
        [242, 24],
        [241, 24],
        [240, 24],
        [239, 24],
        [238, 24],
        [237, 24],
        [236, 24],
        [235, 24],
        [234, 24],
        [233, 24],
        [232, 24],
        [231, 24],
        [230, 24],
        [229, 24],
        [228, 23],
        [229, 22],
        [230, 22],
        [231, 22],
        [232, 22],
        [233, 22],
        [234, 22],
        [235, 21],
        [234, 21],
        [233, 20],
        [232, 20],
        [231, 20],
        [230, 20],
        [229, 19],
        [228, 19],
        [227, 19],
        [226, 19],
        [225, 19],
        [224, 19],
        [223, 19],
        [222, 19],
        [221, 19],
        [220, 19],
        [219, 18],
        [218, 18],
        [217, 18],
        [216, 18],
        [215, 18],
        [214, 18],
        [213, 18],
        [212, 18],
        [211, 18],
        [210, 18],
        [209, 18],
        [208, 18],
        [207, 18],
        [206, 18],
        [205, 18],
        [204, 18],
        [203, 18],
        [202, 18],
        [201, 18],
        [200, 18],
        [199, 18],
        [198, 18],
        [197, 18],
        [196, 18],
        [195, 18],
        [194, 18],
        [193, 18],
        [192, 18],
        [191, 18],
        [190, 18],
        [189, 18],
        [188, 18],
        [187, 18],
        [186, 18],
        [185, 18],
        [184, 18],
        [183, 18],
        [182, 18],
        [181, 18],
        [180, 18],
        [179, 18],
        [178, 18],
        [177, 18],
        [176, 18],
        [175, 18],
        [174, 18],
        [173, 18],
        [172, 18],
        [171, 18],
        [170, 18],
        [169, 18],
        [168, 18],
        [167, 18],
        [166, 18],
        [165, 18],
        [164, 18],
        [163, 18],
        [162, 18],
        [161, 18],
        [160, 18],
        [159, 18],
        [158, 18],
        [157, 18],
        [156, 18],
        [155, 18],
        [154, 18],
        [153, 18],
        [152, 18],
        [151, 18],
        [150, 18],
        [149, 18],
        [148, 18],
        [147, 18],
        [146, 18],
        [145, 18],
        [144, 18],
        [143, 18],
        [142, 19],
        [141, 19],
        [140, 19],
        [139, 19],
        [138, 19],
        [137, 19],
        [136, 19],
        [135, 19],
        [134, 19],
        [133, 20],
        [132, 20],
        [131, 20],
        [130, 20],
        [129, 20],
        [128, 20],
        [127, 21],
        [126, 21],
        [125, 21],
        [124, 21],
        [123, 21],
        [122, 22],
        [121, 22],
        [120, 22],
        [119, 22],
        [118, 23],
        [117, 23],
        [116, 23],
        [115, 24],
        [114, 24],
        [113, 24],
        [112, 25],
        [111, 25],
        [110, 25],
        [109, 26],
        [108, 26],
        [107, 27],
        [106, 27],
        [105, 28],
        [104, 29],
        [103, 29],
        [102, 30],
        [101, 31],
        [100, 32],
        [99, 33],
        [98, 34],
        [97, 35],
        [96, 36],
        [96, 37],
        [95, 38],
        [94, 39],
        [94, 40],
        [93, 41],
        [93, 42],
        [92, 43],
        [92, 44],
        [92, 45],
        [91, 46],
        [91, 47],
        [91, 48],
        [90, 49],
        [90, 50],
        [90, 51],
        [90, 52],
        [90, 53],
        [90, 54],
        [89, 55],
        [89, 56],
        [89, 57],
        [89, 58],
        [89, 59],
        [89, 60],
        [89, 61],
        [89, 62],
        [89, 63],
        [89, 64],
        [89, 65],
        [89, 66],
        [88, 67],
        [88, 68],
        [88, 69],
        [88, 70],
        [88, 71],
        [88, 72],
        [88, 73],
        [88, 74],
        [88, 75],
        [88, 76],
        [87, 77],
        [87, 78],
        [87, 79],
        [87, 80],
        [86, 81],
        [86, 82],
        [86, 83],
        [86, 84],
        [85, 85],
        [85, 86],
        [85, 87],
        [85, 88],
        [84, 89],
        [84, 90],
        [84, 91],
        [84, 92],
        [84, 93],
        [83, 94],
        [83, 95],
        [83, 96],
        [83, 97],
        [83, 98],
        [83, 99],
        [83, 100],
        [82, 101],
        [82, 102],
        [82, 103],
        [82, 104],
        [82, 105],
        [82, 106],
        [82, 107],
        [82, 108],
        [82, 109],
        [82, 110],
        [82, 111],
        [82, 112],
        [82, 113],
        [82, 114],
        [82, 115],
        [82, 116],
        [82, 117],
        [82, 118],
        [82, 119],
        [82, 120],
        [82, 121],
        [82, 122],
        [82, 123],
        [82, 124],
        [82, 125],
        [82, 126],
        [82, 127],
        [83, 128],
        [83, 129],
        [83, 130],
        [83, 131],
        [83, 132],
        [83, 133],
        [84, 134],
        [84, 135],
        [84, 136],
        [84, 137],
        [84, 138],
        [85, 139],
        [85, 140],
        [85, 141],
        [85, 142],
        [86, 143],
        [86, 144],
        [86, 145],
        [86, 146],
        [87, 147],
        [87, 148],
        [87, 149],
        [87, 150],
        [88, 151],
        [88, 152],
        [88, 153],
        [88, 154],
        [88, 155],
        [89, 156],
        [89, 157],
        [89, 158],
        [89, 159],
        [90, 160],
        [90, 161],
        [90, 162],
        [90, 163],
        [90, 164],
        [90, 165],
        [91, 166],
        [91, 167],
        [91, 168],
        [91, 169],
        [91, 170],
        [91, 171],
        [92, 172],
        [92, 173],
        [92, 174],
        [92, 175],
        [92, 176],
        [92, 177],
        [92, 178],
        [92, 179],
        [92, 180],
        [93, 181],
        [93, 182],
        [93, 183],
        [93, 184],
        [93, 185],
        [93, 186],
        [93, 187],
        [93, 188],
        [93, 189],
        [93, 190],
        [93, 191],
        [93, 192],
        [93, 193],
        [93, 194],
        [93, 195],
        [93, 196],
        [93, 197],
        [93, 198],
        [93, 199],
        [93, 200],
        [93, 201],
        [93, 202],
        [92, 203],
        [92, 204],
        [92, 205],
        [92, 206],
        [92, 207],
        [92, 208],
        [92, 209],
        [92, 210],
        [92, 211],
        [92, 212],
        [92, 213],
        [91, 214],
        [91, 215],
        [91, 216],
        [91, 217],
        [91, 218],
        [91, 219],
        [91, 220],
        [90, 221],
        [90, 222],
        [90, 223],
        [90, 224],
        [90, 225],
        [89, 226],
        [89, 227],
        [89, 228],
        [89, 229],
        [88, 230],
        [88, 231],
        [88, 232],
        [87, 233],
        [87, 234],
        [87, 235],
        [86, 236],
        [86, 237],
        [86, 238],
        [85, 239],
        [85, 240],
        [84, 241],
        [84, 242],
        [83, 243],
        [83, 244],
        [82, 245],
        [82, 246],
        [81, 247],
        [80, 248],
        [80, 249],
        [79, 250],
        [78, 251],
        [77, 252],
        [76, 253],
        [75, 254],
        [74, 254],
        [73, 255],
        [72, 256],
        [71, 257],
        [70, 258],
        [69, 258],
        [68, 259],
        [67, 260],
        [66, 261],
        [65, 262],
        [64, 262],
        [63, 263],
        [62, 264],
        [61, 265],
        [60, 265],
        [59, 266],
        [58, 267],
        [57, 268],
        [56, 269],
        [55, 269],
        [54, 270],
        [53, 271],
        [52, 272],
        [51, 273],
        [50, 273],
        [49, 274],
        [48, 275],
        [47, 276],
        [46, 277],
        [45, 278],
        [44, 279],
        [43, 280],
        [42, 281],
        [41, 282],
        [40, 283],
        [39, 284],
        [38, 285],
        [37, 286],
        [37, 287],
        [36, 288],
        [35, 289],
        [34, 290],
        [34, 291],
        [33, 292],
        [32, 293],
        [32, 294],
        [31, 295],
        [30, 296],
        [30, 297],
        [29, 298],
        [29, 299],
        [28, 300],
        [28, 301],
        [27, 302],
        [26, 303],
        [26, 304],
        [26, 305],
        [25, 306],
        [25, 307],
        [24, 308],
        [24, 309],
        [23, 310],
        [23, 311],
        [23, 312],
        [22, 313],
        [22, 314],
        [22, 315],
        [22, 316],
        [21, 317],
        [21, 318],
        [21, 319],
        [21, 320],
        [21, 321],
        [20, 322],
        [20, 323],
        [20, 324],
        [20, 325],
        [20, 326],
        [20, 327],
        [20, 328],
        [20, 329],
        [20, 330],
        [19, 331],
        [19, 332],
        [19, 333],
        [19, 334],
        [19, 335],
        [19, 336],
        [19, 337],
        [19, 338],
        [19, 339],
        [18, 340],
        [17, 341],
        [16, 342],
        [15, 343],
        [14, 344],
        [13, 345],
        [13, 346],
        [12, 347],
        [11, 348],
        [10, 349],
    ]
)
