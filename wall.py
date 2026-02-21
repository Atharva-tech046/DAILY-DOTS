from PIL import Image, ImageDraw
import datetime

# Configuration
WIDTH, HEIGHT = 1179, 2556
BG_COLOR = (0, 0, 0)
DOT_COLOR_DONE = (255, 255, 255)
DOT_COLOR_TODO = (44, 44, 46)
COLS = 15
DOT_SIZE = 25
SPACING = 45

def generate_dots():
    img = Image.new('RGB', (WIDTH, HEIGHT), color=BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Calculate Day of Year
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    
    start_x = (WIDTH - (COLS * SPACING)) // 2
    start_y = 600

    for i in range(365):
        x = start_x + (i % COLS) * SPACING
        y = start_y + (i // COLS) * SPACING
        
        color = DOT_COLOR_DONE if i < day_of_year else DOT_COLOR_TODO
        draw.ellipse([x, y, x + DOT_SIZE, y + DOT_SIZE], fill=color)
    
    img.save("wallpaper.png")

if __name__ == "__main__":
    generate_dots()
    