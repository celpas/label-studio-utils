import json
import logging
import os
import uuid

logger = logging.getLogger(__name__)

COLORS = [
    (218, 1, 238),
    (0, 255, 0),
    (1, 146, 243),
    (241, 135, 0),
    (12, 0, 184),
    (72, 124, 73),
    (187, 1, 37),
    (166, 250, 86),
    (178, 135, 216),
    (0, 252, 159),
    (116, 239, 254),
    (252, 65, 124),
    (99, 56, 252),
    (252, 183, 127),
    (115, 41, 127),
    (255, 255, 0),
    (137, 176, 1),
    (95, 192, 153),
    (1, 53, 87),
    (148, 86, 0),
    (179, 123, 99),
    (5, 168, 6),
    (33, 101, 165),
    (3, 232, 254),
    (254, 86, 239),
    (64, 234, 74),
    (188, 228, 185),
    (45, 74, 0),
    (2, 170, 123),
    (251, 53, 7),
    (250, 176, 247),
    (176, 61, 197),
    (127, 255, 0),
    (99, 1, 6),
    (199, 4, 140),
    (0, 71, 252),
    (101, 164, 251),
    (255, 255, 127),
    (215, 197, 46),
    (117, 3, 199),
    (70, 0, 82),
    (116, 120, 156),
    (244, 121, 164),
    (147, 186, 88),
    (183, 55, 82),
    (96, 253, 180),
    (19, 194, 191),
    (0, 0, 255),
    (254, 7, 79),
    (77, 135, 0),
    (103, 62, 54),
    (82, 111, 222),
    (254, 121, 80),
    (176, 195, 252),
    (60, 215, 6),
    (53, 50, 196),
    (186, 168, 150),
    (52, 180, 59),
    (2, 108, 105),
    (5, 3, 119),
    (1, 117, 28),
    (248, 34, 189),
    (212, 92, 35),
    (252, 216, 188),
    (74, 3, 252),
    (255, 0, 0),
    (193, 245, 20),
    (139, 130, 41),
    (1, 223, 106),
    (72, 85, 115),
    (147, 0, 96),
    (160, 22, 253),
    (144, 96, 251),
    (64, 149, 178),
    (182, 254, 244),
    (47, 30, 32),
    (5, 51, 149),
    (138, 176, 198),
    (71, 5, 144),
    (2, 216, 42),
    (73, 208, 226),
    (109, 235, 121),
    (161, 87, 139),
    (120, 221, 46),
    (114, 73, 187),
    (149, 33, 8),
    (207, 218, 117),
    (42, 253, 212),
    (189, 154, 12),
    (1, 0, 56),
    (106, 154, 114),
    (230, 130, 245),
    (3, 149, 73),
    (210, 52, 252),
    (254, 234, 63),
    (216, 159, 83),
    (52, 227, 152),
    (211, 187, 204),
    (0, 142, 181),
    (44, 76, 58),
    (127, 98, 89),
    (149, 209, 148),
    (52, 130, 124),
    (0, 102, 212),
    (58, 198, 109),
    (196, 50, 141),
    (252, 163, 185),
    (254, 207, 3),
    (177, 15, 195),
    (27, 187, 253),
    (224, 79, 187),
    (130, 221, 204),
    (225, 216, 252),
    (251, 0, 149),
    (203, 47, 28),
    (254, 167, 43),
    (94, 96, 17),
    (242, 49, 67),
    (155, 253, 146),
    (63, 42, 96),
    (104, 166, 48),
    (189, 122, 160),
    (35, 36, 247),
    (195, 93, 238),
    (1, 253, 68),
    (217, 95, 107),
    (140, 4, 150),
    (117, 13, 55),
    (93, 45, 0),
    (0, 58, 28),
    (80, 254, 28),
    (165, 200, 34),
    (123, 134, 205),
    (34, 111, 254),
    (208, 18, 86),
    (254, 35, 248),
    (228, 251, 199),
    (64, 2, 202),
    (65, 50, 144),
    (164, 87, 53),
    (113, 254, 75),
    (1, 40, 205),
    (218, 254, 88),
    (154, 98, 193),
    (58, 147, 230),
    (47, 254, 117),
    (145, 137, 254),
    (249, 95, 1),
    (78, 177, 4),
    (128, 42, 216),
    (207, 253, 146),
    (150, 143, 134),
    (52, 78, 230),
    (153, 41, 162),
    (137, 42, 83),
    (185, 112, 1),
    (121, 200, 246),
    (173, 158, 61),
    (10, 203, 146),
    (203, 127, 53),
    (109, 210, 1),
    (43, 143, 38),
    (51, 176, 146),
    (71, 254, 252),
    (221, 145, 132),
    (7, 188, 82),
    (100, 198, 82),
    (90, 179, 200),
    (101, 34, 172),
    (1, 228, 205),
    (205, 163, 245),
    (200, 210, 0),
    (111, 157, 166),
    (152, 254, 208),
    (22, 73, 118),
    (165, 62, 254),
    (254, 84, 59),
    (58, 162, 100),
    (227, 16, 33),
    (233, 30, 124),
    (247, 200, 81),
    (167, 29, 114),
    (230, 177, 1),
    (212, 149, 187),
    (224, 5, 188),
    (153, 248, 40),
    (181, 210, 79),
    (121, 1, 247),
    (115, 78, 140),
    (224, 201, 157),
    (84, 30, 222),
    (33, 248, 35),
    (6, 124, 142),
    (80, 97, 157),
    (216, 113, 201),
    (24, 109, 67)]


LABELING_CONFIG = """<View>
  <Image name="{# TO_NAME #}" zoom="true" zoomControl="true" maxWidth="1500px"/>
  <RectangleLabels name="{# FROM_NAME #}" toName="image">

{# LABELS #}
  </RectangleLabels>
</View>
"""


def generate_label_config(categories, to_name='image', from_name='label', filename=None):
    labels = ''
    for key in sorted(categories.keys()):
        color = COLORS[key % len(COLORS)]
        label = f'    <Label value="{categories[key]}" background="rgba({color[0]}, {color[1]}, {color[2]}, 1)"/>\n'
        labels += label

    config = LABELING_CONFIG \
        .replace('{# LABELS #}', labels) \
        .replace('{# TO_NAME #}', to_name) \
        .replace('{# FROM_NAME #}', from_name)

    if filename:
        with open(filename, 'w') as f:
            f.write(config)

    return config


def new_task(out_type, root_url, file_name):
    return {
        "data": {
            "image": os.path.join(root_url, file_name)
        },
        # 'annotations' or 'predictions'
        out_type: [
            {
                "result": [],
                "ground_truth": False,
            }
        ]
    }


def convert_coco_to_ls(input_file, out_file,
                       to_name='image', from_name='label', out_type="annotations",
                       image_root_url='/data/local-files/?d=',
                       use_super_categories=False):

    """ Convert COCO labeling to Label Studio JSON

    :param input_file: file with COCO json
    :param out_file: output file with Label Studio JSON tasks
    :param to_name: object name from Label Studio labeling config
    :param from_name: control tag name from Label Studio labeling config
    :param out_type: annotation type - "annotations" or "predictions"
    :param image_root_url: root URL path where images will be hosted, e.g.: http://example.com/images
    :param use_super_categories: use super categories from categories if they are presented
    """

    tasks = {}  # image_id => task
    logger.info('Reading COCO notes and categories from %s', input_file)

    with open(input_file, encoding='utf8') as f:
        coco = json.load(f)

    # build categories => labels dict
    new_categories = {}
    # list to dict conversion: [...] => {category_id: category_item}
    categories = {category['id']: category for category in coco['categories']}
    ids = sorted(categories.keys())  # sort labels by their origin ids

    for i in ids:
        name = categories[i]['name']
        if use_super_categories and 'supercategory' in categories[i]:
            name = categories[i]['supercategory'] + ':' + name
        new_categories[i] = name

    # mapping: id => category name
    categories = new_categories

    # mapping: image id => image
    images = {item['id']: item for item in coco['images']}

    logger.info(f'Found {len(categories)} categories, {len(images)} images and {len(coco["annotations"])} annotations')

    # generate and save labeling config
    label_config_file = out_file.replace('.json', '') + '.label_config.xml'
    generate_label_config(categories, to_name, from_name, label_config_file)

    # flags for labeling config composing
    segmentation = bbox = keypoints = rle = False
    rle_once, segmentation_once, keypoints_once = False, False, False

    for i, annotation in enumerate(coco['annotations']):
        segmentation |= 'segmentation' in annotation
        bbox |= 'bbox' in annotation
        keypoints |= 'keypoints' in annotation
        rle |= annotation['iscrowd'] == 1  # 0 - polygons are inside of segmentation, otherwise rle

        # not supported
        if rle and not rle_once:
            logger.warning('RLE in segmentation is not yet supported in COCO')
            rle_once = True
        if keypoints and not keypoints_once:
            logger.warning('Keypoints are partially supported without skeletons')
            keypoints_once = True
        # not supported
        if segmentation and not segmentation_once:
            logger.warning('Segmentation is not yet supported in COCO')
            segmentation_once = True

        # read image sizes
        image_id = annotation['image_id']
        image = images[image_id]
        image_file_name, image_width, image_height = image['file_name'], image['width'], image['height']

        # get or create new task
        task = tasks[image_id] if image_id in tasks else new_task(out_type, image_root_url, image_file_name)

        if 'bbox' in annotation:
            # convert all bounding boxes to Label Studio Results
            label = categories[int(annotation['category_id'])]
            x, y, width, height = annotation['bbox']
            x, y, width, height = float(x), float(y), float(width), float(height)
            item = {
                "id": uuid.uuid4().hex[0:10],
                "type": "rectanglelabels",
                "value": {
                    "x": x / image_width * 100.0,
                    "y": y / image_height * 100.0,
                    "width": width / image_width * 100.0,
                    "height": height / image_height * 100.0,
                    "rotation": 0,
                    "rectanglelabels": [
                        label
                    ]
                },
                "to_name": to_name,
                "from_name": from_name,
                "image_rotation": 0,
                "original_width": image_width,
                "original_height": image_height
            }
            task[out_type][0]['result'].append(item)

        tasks[image_id] = task

    if len(tasks) > 0:
        tasks = [tasks[key] for key in sorted(tasks.keys())]
        logger.info('Saving Label Studio JSON to %s', out_file)
        with open(out_file, 'w') as out:
            json.dump(tasks, out)

        print('\n'
              f'  1. Create a new project in Label Studio\n'
              f'  2. Use Labeling Config from "{label_config_file}"\n'
              f'  3. Setup serving for images [e.g. you can use Local Storage (or others):\n'
              f'     https://labelstud.io/guide/storage.html#Local-storage]\n'
              f'  4. Import "{out_file}" to the project\n')
    else:
        logger.error('No labels converted')
