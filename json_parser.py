import json

SIZE = 512

with open('coco_data/coco_annotations.json') as f:
    data = json.load(f)
    annotations = data.get("annotations")
    for item in annotations:
        item.pop('segmentation')

    # We get every item as coco_annotation counts the PLANE as a label
    # I'm sure there's better way around this.
    for i in range(1, len(annotations), 2):
        bbox = annotations[i].get("bbox")
        # We normalise by the size of the image- 512 x 512
        bbox = [coords / SIZE for coords in bbox]
        category_id = annotations[i].get("category_id") 
        # YOLO wants correctly named class numbers
        category_id = 0
        bbox_str = ' '.join([str(coords) for coords in bbox])
        output = str(category_id) + " " + bbox_str
        
        img_id = annotations[i].get("image_id")
        with open(f'coco_data/labels/{img_id:06}.txt', 'w') as out:
            out.write(output)