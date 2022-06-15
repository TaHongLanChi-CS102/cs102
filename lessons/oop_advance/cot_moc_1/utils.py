from typing import Tuple

import pygame
from pygame import Surface


def scale_image(image: Surface, scale: float) -> Surface:
    """Resize image by a factor of input arg `scale`."""
    new_dimension: Tuple[int, int] = (
        int(image.get_width() * scale),
        int(image.get_height() * scale),
    )
    return pygame.transform.scale(image, new_dimension)


def overlap(x1: float, y1: float, image1: Surface, x2: float, y2: float, image2: Surface) -> bool:
    """Returns True if 2 items overlap."""
    mask1 = pygame.mask.from_surface(image1)
    mask2 = pygame.mask.from_surface(image2)
    offset_x = x2 - x1
    offset_y = y2 - y1
    return bool(mask1.overlap(mask2, (offset_x, offset_y)))
