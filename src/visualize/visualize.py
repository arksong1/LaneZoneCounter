import cv2

def draw_boxes(frame, detections, class_names):
    for detection in detections:
        x1, y1, x2, y2 = map(int, detection["bbox"])
        conf = detection["conf"]
        cls_id = detection["class"]

        label = class_names[cls_id] 
        text = f"{label} - {detection['track_id']} - {conf: .2f}"

        box_color = (0, 0 ,255)

        # Vẽ box
        cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, 2)

        (width_text, height_text), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)

        # Background text
        cv2.rectangle(frame, (x1, y1 - height_text - 6), (x1 + width_text, y1), box_color, -1)

        cv2.putText(
            frame,
            text,
            (x1, y1 - 2),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            1,
            cv2.LINE_AA
        ) # frame, text, vi tri text, font, scale, color, do day, mau sac, line type

    return frame

