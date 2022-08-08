# Importing necessary libraries

import os
import numpy as np
import cv2

if __name__ == "__main__":

  # Creating folders for storing input and output (ground truth) images 

  input_path = 'Shape_Filling_AI\Input'
  output_path = 'Shape_Filling_AI\Output'
  os.makedirs(input_path, exist_ok = True)
  os.makedirs(output_path, exist_ok = True)

  # Rectangles

  shape = 'rectangle'

  for i in range(1000):
    img = np.zeros((256, 256, 1))

    # Generating rectangles with random locations and dimensions
    start_point = (int(np.random.randint(256, size=1)), int(np.random.randint(256, size=1)))
    end_point = (int(np.random.randint(256, size=1)), int(np.random.randint(256, size=1)))
    color = 255
    
    # Drawing the boundary of the figure - input
    image = cv2.rectangle(img, start_point, end_point, color, thickness = 1)
    cv2.imwrite('{}/{}_{}.png'.format(input_path, shape, i), image)

    # Drawing the corresponding filled figure - output
    image = cv2.rectangle(img, start_point, end_point, color, thickness = -1)
    cv2.imwrite('{}/{}_{}.png'.format(output_path, shape, i), image)


  # Triangle

  shape = 'triangle'

  for i in range(1000):
    img = np.zeros((256, 256, 1))

    # Generating triangles with random locations and dimensions
    p1 = (int(np.random.randint(256, size=1)), int(np.random.randint(256, size=1)))
    p2 = (int(np.random.randint(256, size=1)), int(np.random.randint(256, size=1)))
    p3 = (int(np.random.randint(256, size=1)), int(np.random.randint(256, size=1)))
    cv2.line(img, p1, p2, (255, 255, 255), 1)
    cv2.line(img, p2, p3, (255, 255, 255), 1)
    cv2.line(img, p1, p3, (255, 255, 255), 1)

    # Drawing the boundary of the figure - input
    cv2.imwrite('{}/{}_{}.png'.format(input_path, shape, i), img)

    # Drawing the corresponding filled figure - output
    points = np.array([p1, p2, p3])
    cv2.fillPoly(img, pts=[points], color=(255, 255, 255))
    cv2.imwrite('{}/{}_{}.png'.format(output_path, shape, i), img)


  # Ellipse

  shape = "ellipse"
  for i in range(1000):
      img = np.zeros((256, 256, 1))

      # Generating ellipses with random center coordinates and axes length to provide variety in locations and dimensions
      center_coordinates = (int(np.random.randint(150, size=1)), int(np.random.randint(150, size=1)))
      axesLength = (int(np.random.randint(100, size=1)), int(np.random.randint(100, size=1)))
      
      # Drawing the boundary of the figure - input
      image = cv2.ellipse(img, center_coordinates, axesLength,
            angle = 0, startAngle = 0, endAngle = 360, 
            color = (255, 255, 255), thickness = 1)
      cv2.imwrite('{}/{}_{}.png'.format(input_path, shape, i), image)

      # Drawing the corresponding filled figure - output
      image = cv2.ellipse(img, center_coordinates, axesLength,
            angle = 0, startAngle = 0, endAngle = 360, 
            color = (255, 255, 255), thickness = -1)
      cv2.imwrite('{}/{}_{}.png'.format(output_path, shape, i), image)


  # Circle

  shape = "circle"
  for i in range(1000):
      img = np.zeros((256, 256, 1))

      # Generating circles with random center coordinates and radius to provide variety in locations and dimensions
      center_coordinates = (int(np.random.randint(175, size=1)), int(np.random.randint(175, size=1)))
      radius = int(np.random.randint((50, 175), size=1))
      color = 255
      
      # Drawing the boundary of the figure - input
      image = cv2.circle(img, center_coordinates, radius, color, thickness = 1)
      cv2.imwrite('{}/{}_{}.png'.format(input_path, shape, i), image)
      
      # Drawing the corresponding filled figure - output
      image = cv2.circle(img, center_coordinates, radius, color, thickness = -1)
      cv2.imwrite('{}/{}_{}.png'.format(output_path, shape, i), image)

  # Random_Pentagons

  shape = 'pentagon'
  for i in range(1000):
      img = np.zeros((256, 256, 1))

      # Generating pentagons with random locations and dimensions
      p1 = [int(np.random.randint(256, size=1)), int(np.random.randint(256, size=1))]
      p2 = [int(np.random.randint(256, size=1)), int(np.random.randint(256, size=1))]
      p3 = [int(np.random.randint(256, size=1)), int(np.random.randint(256, size=1))]
      p4 = [int(np.random.randint(256, size=1)), int(np.random.randint(256, size=1))]
      p5 = [int(np.random.randint(256, size=1)), int(np.random.randint(256, size=1))]
      cv2.line(img, p1, p2, (255, 255, 255), 1)
      cv2.line(img, p2, p3, (255, 255, 255), 1)
      cv2.line(img, p3, p4, (255, 255, 255), 1)
      cv2.line(img, p4, p5, (255, 255, 255), 1)
      cv2.line(img, p5, p1, (255, 255, 255), 1)  
  
      # Drawing the boundary of the figure - input    
      cv2.imwrite('{}/{}_{}.png'.format(input_path, shape, i), img)
      
      # Drawing the corresponding filled figure - output
      points = np.array([p1, p2, p3, p4, p5])
      cv2.fillPoly(img, pts=[points], color=(255, 255, 255))
      cv2.imwrite('{}/{}_{}.png'.format(output_path, shape, i), img)


  # STAR

  shape = 'star'
  for i in range(1000):
    img = np.zeros((256, 256, 1))

    # Points for generating the boundary of a star without interior lines.
    points = np.array([[160,  40], [177,  95], [236,  95], [189,  130], [207,  185], [160 ,150], 
                      [113,  185], [131,  130], [84, 95], [142, 95]])

    # Random shifts to provide variability in location and rotation.
    shift = int(np.random.randint(low = -100, high=50, size=1))
    points = points + shift

    # Drawing the boundary of the figure - input
    for j in range(0, len(points)):
      if (j!= len(points) - 1):
        cv2.line(img, points[j], points[j+1], 255, 1)
      else:
        cv2.line(img, points[j], points[0], 255, 1)  
    cv2.imwrite('{}/{}_{}.png'.format(input_path, shape, i), img)

    # Drawing the corresponding filled figure - output
    img = cv2.fillPoly(img, [points], color = (255, 255, 255))
    cv2.imwrite('{}/{}_{}.png'.format(output_path, shape, i), img)


  # Random open figures, lines, squiggles, and dots

  # 2 - points

  shape = "random_2_points"
  for i in range(500):
    img = np.zeros((256, 256, 1))
    p1 = [int(np.random.randint(256, size=1)), int(np.random.randint(256, size=1))]
    p2 = [int(np.random.randint(256, size=1)), int(np.random.randint(256, size=1))]

    # Drawing the boundary of the open figure - input and output (since no filling/inpainting is required)
    cv2.line(img, p1, p2, (255, 255, 255), 1)
    cv2.imwrite('{}/{}_{}.png'.format(input_path, shape, i), img)
    cv2.imwrite('{}/{}_{}.png'.format(output_path, shape, i), img)

  # 3 - points

  shape = "random_3_points"
  for i in range(500):
    img = np.zeros((256, 256, 1))
    p1 = [int(np.random.randint(256, size=1)), int(np.random.randint(256, size=1))]
    p2 = [int(np.random.randint(256, size=1)), int(np.random.randint(256, size=1))]
    p3 = [int(np.random.randint(256, size=1)), int(np.random.randint(256, size=1))]

    cv2.line(img, p1, p2, (255, 255, 255), 1)
    cv2.line(img, p2, p3, (255, 255, 255), 1)

    # Drawing the boundary of the open figure - input and output (since no filling/inpainting is required)
    cv2.imwrite('{}/{}_{}.png'.format(input_path, shape, i), img)
    cv2.imwrite('{}/{}_{}.png'.format(output_path, shape, i), img)
