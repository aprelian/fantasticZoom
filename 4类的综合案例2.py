import pygame
from random import randint
from pygame.locals import *

SCREEN_SIZE = (1040, 680)
NEST_POSITION = (320, 340)
ANT_COUNT = 20
NEST_SIZE = 280.


class World:
    def __init__(self):
        self.entities = {}
        self.entity_id = 0
        self.background = pygame.Surface(SCREEN_SIZE).convert()
        self.background.fill((155, 255, 155))
        pygame.draw.circle(self.background, (200, 155, 200), NEST_POSITION, int(NEST_SIZE))

    # def add_entity(self, entity):
    #     self.entities[self.entity_id] = entity
    #     entity.id = self.entity_id
    #     self.entity_id += 1
    #     print(self.entity_id, entity.name)
    def __setitem__(self, key, value):
        self.entities[key] = value
        value.id = self.entity_id
        print(self.entity_id, value.name)
        self.entity_id += 1

    #
    def remove_entity(self, entity):
        del self.entities[entity.id]

    def get(self, entity_id):
        if entity_id in self.entities:
            return self.entities[entity_id]
        else:
            return None
    #
    def process(self, time_passed):
        time_passed_seconds = time_passed / 500.0
        for entity in list(self.entities.values()):
            entity.process(time_passed_seconds)

    def render(self, surface):
        surface.blit(self.background, (0, 0))
        for entity in self.entities.values():
            entity.render(surface)
    #
    def get_close_entity(self, name, location, range=200.):
        location = Vector2(*location)
        for entity in self.entities.values():
            if entity.name == name:
                distance = location.get_distance_to(entity.location)
                if distance < range:
                    return entity
        return None
class State:
    def __init__(self, name):
        self.name = name
    def do_actions(self):
        pass
    def check_conditions(self):
        pass
    def entry_actions(self):
        pass
    def exit_actions(self):
        pass

class Brain:
    def __init__(self):
        self.states = {}
        self.active_state = None

    def add_state(self, state):
        self.states[state.name] = state

    def think(self):
        if self.active_state is None:
            return
        self.active_state.do_actions()
        new_state_name = self.active_state.check_conditions()
        if new_state_name is not None:
            self.set_state(new_state_name)

    def set_state(self, new_state_name):
        if self.active_state is not None:
            self.active_state.exit_actions()
        self.active_state = self.states[new_state_name]
        self.active_state.entry_actions()

class Vector2(object):
    def __init__(self, x=0., y=0.):
        """Initialise a vector
        """
        if hasattr(x, "__getitem__"):
            x, y = x
            self._v = [float(x), float(y)]
        else:
            self._v = [float(x), float(y)]
    # @classmethod
    # def from_points(cls, p1, p2):
    #     """Creates a Vector2 object between two points.
    #     @param p1: First point
    #     @param p2: Second point
    #
    #     """
    #     v = cls.__new__(cls, object)
    #     x, y = p1
    #     xx, yy = p2
    #     v._v = [float(xx-x), float(yy-y)]
    #     return v
    # def _get_length(self):
    #     x, y = self._v
    #     return (x*x + y*y)**0.5
    # def _set_length(self, length):
    #     v = self._v
    #     try:
    #         x, y = v
    #         l = length / (x*x +y*y)**0.5
    #     except ZeroDivisionError:
    #         v[0] = 0.0
    #         v[1] = 0.0
    #         return self
    #     v[0] *= l
    #     v[1] *= l
    # length = property(_get_length, _set_length, None, "Length of the vector")


    @classmethod
    def from_floats(cls, x, y):
        vec = cls.__new__(cls, object)
        vec._v = [x, y]
        return vec
    #
    #
    # @classmethod
    # def from_iter(cls, iterable):
    #     """Creates a Vector2 object from an iterable.
    #
    #     @param iterable: An iterable of at least 2 numeric values
    #
    #     """
    #     next = iter(iterable).next
    #     vec = cls.__new__(cls, object)
    #     vec._v = [float(next()), float(next())]
    #     return vec


    # @classmethod
    # def from_points(cls, p1, p2):
    #     """Creates a Vector2 object between two points.
    #     @param p1: First point
    #     @param p2: Second point
    #
    #     """
    #     v = cls.__new__(cls, object)
    #     x, y = p1
    #     xx, yy = p2
    #     v._v = [float(xx-x), float(yy-y)]
    #     return v

    # @classmethod
    # def _from_float_sequence(cls, sequence):
    #     v = cls.__new__(cls, object)
    #     v._v = list(sequence[:2])
    #     return v
    #
    #
    # def copy(self):
    #     """Returns a copy of this object."""
    #     vec = self.__new__(self.__class__, object)
    #     vec._v = self._v[:]
    #     return vec

    # def get_x(self):
    #     return self._v[0]
    # def set_x(self, x):
    #     try:
    #         self._v[0] = 1.0 * x
    #     except:
    #         raise TypeError("Must be a number")
    # x = property(get_x, set_x, None, "x component.")

    # def get_y(self):
    #     return self._v[1]
    # def set_y(self, y):
    #     try:
    #         self._v[1] = 1.0 * y
    #     except:
    #         raise TypeError("Must be a number")
    # y = property(get_y, set_y, None, "y component.")

    #u = property(get_x, set_y, None, "u component (alias for x).")
    #v = property(get_y, set_y, None, "v component (alias for y).")

    # def __str__(self):
    #
    #     x, y = self._v
    #     return "(%s, %s)" % (x, y)
    #
    # def __repr__(self):
    #
    #     x, y = self._v
    #     return "Vector2(%s, %s)" % (x, y)
    #
    def __iter__(self):

        return iter(self._v[:])
    #
    # def __len__(self):
    #
    #     return 2


    def __getitem__(self, index):
        """Gets a component as though the vector were a list."""
        try:
            return self._v[index]
        except IndexError:
            print("There are 2 values in this object, index should be 0 or 1")

    def __setitem__(self, index, value):
        """Sets a component as though the vector were a list."""

        try:
            self._v[index] = 1.0 * value
        except IndexError:
            print("There are 2 values in this object, index should be 0 or 1!")
        except TypeError:
            print("Must be a number")


    # def __eq__(self, rhs):
    #     x, y = self._v
    #     xx, yy = rhs
    #     return x == xx and y == yy
    #
    def __ne__(self, rhs):
        x, y = self._v
        xx, yy, = rhs
        return x != xx or y != yy
    #
    # def __hash__(self):
    #
    #     return hash(self._v)

    def __add__(self, rhs):
        x, y = self._v
        xx, yy = rhs
        return Vector2.from_floats(x+xx, y+yy)
    #
    #
    # def __iadd__(self, rhs):
    #     xx, yy = rhs
    #     v = self._v
    #     v[0] += xx
    #     v[1] += yy
    #     return self
    #
    # def __radd__(self, lhs):
    #     x, y = self._v
    #     xx, yy = lhs
    #     return self.from_floats(x+xx, y+yy)

    def __sub__(self, rhs):
        x, y = self._v
        xx, yy = rhs
        return Vector2.from_floats(x-xx, y-yy)
    #
    # def __rsub__(self, lhs):
    #     x, y = self._v
    #     xx, yy = lhs
    #     return self.from_floats(xx-x, yy-y)
    #
    # def _isub__(self, rhs):
    #
    #     xx, yy = rhs
    #     v = self._v
    #     v[0] -= xx
    #     v[1] -= yy
    #     return self


    # def __mul__(self, rhs):
    #     """Return the result of multiplying this vector with a scalar or a vector-list object."""
    #     x, y = self._v
    #     if hasattr(rhs, "__getitem__"):
    #         xx, yy = rhs
    #         return Vector2.from_floats(x*xx, y*yy)
    #     else:
    #         return Vector2.from_floats(x*rhs, y*rhs)


    # def __imul__(self, rhs):
    #     """Multiplys this vector with a scalar or a vector-list object."""
    #     if hasattr(rhs, "__getitem__"):
    #         xx, yy = rhs
    #         v = self._v
    #         v[0] *= xx
    #         v[1] *= yy
    #     else:
    #         v = self._v
    #         v[0] *= rhs
    #         v[1] *= rhs
    #     return self
    #
    def __rmul__(self, lhs):

        x, y = self._v
        if hasattr(lhs, "__getitem__"):
            xx, yy = lhs
        else:
            xx = lhs
            yy = lhs
        return self.from_floats(x*xx, y*yy)


    # def __div__(self, rhs):
    #     """Return the result of dividing this vector by a scalar or a vector-list object."""
    #     x, y = self._v
    #     if hasattr(rhs, "__getitem__"):
    #         xx, yy, = rhs
    #         return Vector2.from_floats(x/xx, y/yy)
    #     else:
    #         return Vector2.from_floats(x/rhs, y/rhs)


    # def __idiv__(self, rhs):
    #     """Divides this vector with a scalar or a vector-list object."""
    #     if hasattr(rhs, "__getitem__"):
    #         xx, yy = rhs
    #         v = self._v
    #         v[0] /= xx
    #         v[1] /= yy
    #     else:
    #         v = self._v
    #         v[0] /= rhs
    #         v[1] /= rhs
    #     return self

    # def __rdiv__(self, lhs):
    #
    #     x, y = self._v
    #     if hasattr(lhs, "__getitem__"):
    #         xx, yy = lhs
    #     else:
    #         xx = lhs
    #         yy = lhs
    #     return self.from_floats(xx/x, yy/x)
    #
    # def __neg__(self):
    #     """Return the negation of this vector."""
    #     x, y = self._v
    #     return Vector2.from_floats(-x, -y)

    # def __pos__(self):
    #
    #     return self.copy()
    #
    # def __nonzero__(self):
    #
    #     x, y = self._v
    #     return bool(x or y)

    # def __call__(self, keys):
    #
    #     """Used to swizzle a vector.
    #
    #     @type keys: string
    #     @param keys: A string containing a list of component names
    #     # >>> vec = Vector(1, 2)
    #     # >>> vec('yx')
    #     (1, 2)
    #
    #     """
    #
    #     ord_x = ord('x')
    #     v = self._v
    #     return tuple( v[ord(c) - ord_x] for c in keys )


    # def as_tuple(self):
    #     """Converts this vector to a tuple.
    #
    #     @rtype: Tuple
    #     @return: Tuple containing the vector components
    #     """
    #     return tuple(self._v)


    def get_length(self):
        """Returns the length of this vector."""
        x, y = self._v
        return (x*x + y*y)**0.5
    get_magnitude = get_length


    # def normalise(self):
    #     """Normalises this vector."""
    #     v = self._v
    #     x, y = v
    #     l = (x*x +y*y)**0.5
    #     try:
    #         v[0] /= l
    #         v[1] /= l
    #     except ZeroDivisionError:
    #         v[0] = 0.
    #         v[1] = 0.
    #     return self
    # normalize = normalise

    def get_normalised(self):
        x, y = self._v
        l = (x*x +y*y)**0.5
        return Vector2.from_floats(x/l, y/l)
    get_normalized = get_normalised

    def get_distance_to(self, p):
        """Returns the distance to a point.

        @param: A Vector2 or list-like object with at least 2 values.
        @return: distance
        """
        x, y = self._v
        xx, yy = p
        dx = xx-x
        dy = yy-y
        return (dx*dx + dy*dy)**0.5


class GameEntity(object):

    def __init__(self, world, name, image):
        self.world = world
        self.name = name
        self.image = image
        self.location = Vector2(0, 0)
        self.destination = Vector2(0, 0)
        self.speed = 0.5
        self.brain = Brain()
        self.id = 0

    def render(self, surface):
        x, y = self.location
        w, h = self.image.get_size()
        surface.blit(self.image, (x - w / 2, y - h / 2))

    def process(self, time_passed):
        self.brain.think()
        if self.speed > 0. and self.location != self.destination:
            vec_to_destination = self.destination - self.location
            distance_to_destination = vec_to_destination.get_length()
            heading = vec_to_destination.get_normalized()
            travel_distance = min(distance_to_destination, time_passed * self.speed)
            self.location += travel_distance * heading

class Leaf(GameEntity):
    def __init__(self, world, image):
        GameEntity.__init__(self, world, "leaf", image)


class Spider(GameEntity):
    def __init__(self, world, image):
        GameEntity.__init__(self, world, "spider", image)
        self.dead_image = pygame.transform.flip(image, 0, 1)
        self.health = 25
        self.speed = 40. + randint(-30, 20)

    def bitten(self):
        self.health -= 2
        if self.health <= 0:
            self.speed = 0.
            self.image = self.dead_image
        self.speed = 120.

    def render(self, surface):
        GameEntity.render(self, surface)
        x, y = self.location
        w, h = self.image.get_size()
        bar_x = x - 12
        bar_y = y + h / 2
        surface.fill((255, 0, 0), (bar_x, bar_y, 25, 4))
        surface.fill((0, 255, 0), (bar_x, bar_y, self.health, 4))

    def process(self, time_passed):
        x, y = self.location
        if x > SCREEN_SIZE[0] + 2:
            self.world.remove_entity(self)
            return
        GameEntity.process(self, time_passed)


class Ant(GameEntity):
    def __init__(self, world, image):
        GameEntity.__init__(self, world, "ant", image)
        exploring_state = AntStateExploring(self)
        seeking_state = AntStateSeeking(self)
        delivering_state = AntStateDelivering(self)
        hunting_state = AntStateHunting(self)
        self.brain.add_state(exploring_state)
        self.brain.add_state(seeking_state)
        self.brain.add_state(delivering_state)
        self.brain.add_state(hunting_state)
        self.carry_image = None

    def carry(self, image):
        self.carry_image = image

    def drop(self, surface):
        if self.carry_image:
            x, y = self.location
            w, h = self.carry_image.get_size()
            surface.blit(self.carry_image, (x - w, y - h / 2))
            self.carry_image = None

    def render(self, surface):
        GameEntity.render(self, surface)
        if self.carry_image:
            x, y = self.location
            w, h = self.carry_image.get_size()
            surface.blit(self.carry_image, (x - w, y - h / 2))

class AntStateExploring(State):
    def __init__(self, ant):
        State.__init__(self, "exploring")
        self.ant = ant

    def random_destination(self):
        w, h = SCREEN_SIZE
        self.ant.destination = Vector2(randint(0, w), randint(0, h))

    def do_actions(self):
        if randint(1, 20) == 1:
            self.random_destination()

    def check_conditions(self):
        leaf = self.ant.world.get_close_entity("leaf", self.ant.location)
        if leaf is not None:
            self.ant.leaf_id = leaf.id
            return "seeking"
        spider = self.ant.world.get_close_entity("spider", NEST_POSITION, NEST_SIZE)
        if spider is not None:
            if self.ant.location.get_distance_to(spider.location) < 100.:
                self.ant.spider_id = spider.id
                return "hunting"
        return None

    def entry_actions(self):
        self.ant.speed = 120. + randint(-30, 30)
        self.random_destination()


class AntStateSeeking(State):
    def __init__(self, ant):
        State.__init__(self, "seeking")
        self.ant = ant
        self.leaf_id = None

    def check_conditions(self):
        leaf = self.ant.world.get(self.ant.leaf_id)
        if leaf is None:
            return "exploring"
        if self.ant.location.get_distance_to(leaf.location) < 5.0:
            self.ant.carry(leaf.image)
            self.ant.world.remove_entity(leaf)
            return "delivering"
        return None

    def entry_actions(self):
        leaf = self.ant.world.get(self.ant.leaf_id)
        if leaf is not None:
            self.ant.destination = leaf.location
            self.ant.speed = 160. + randint(-20, 20)


class AntStateDelivering(State):
    def __init__(self, ant):
        State.__init__(self, "delivering")
        self.ant = ant

    def check_conditions(self):
        if Vector2(*NEST_POSITION).get_distance_to(self.ant.location) < NEST_SIZE:
            if (randint(1, 10) == 1):
                self.ant.drop(self.ant.world.background)
                return "exploring"
        return None

    def entry_actions(self):
        self.ant.speed = 60.
        random_offset = Vector2(randint(-20, 20), randint(-20, 20))
        self.ant.destination = Vector2(*NEST_POSITION) + random_offset


class AntStateHunting(State):
    def __init__(self, ant):
        State.__init__(self, "hunting")
        self.ant = ant
        self.got_kill = False

    def do_actions(self):
        spider = self.ant.world.get(self.ant.spider_id)
        if spider is None:
            return
        self.ant.destination = spider.location
        if self.ant.location.get_distance_to(spider.location) < 15.:
            if randint(1, 5) == 1:
                spider.bitten()
                if spider.health <= 0:
                    self.ant.carry(spider.image)
                    self.ant.world.remove_entity(spider)
                    self.got_kill = True

    def check_conditions(self):
        if self.got_kill:
            return "delivering"
        spider = self.ant.world.get(self.ant.spider_id)
        if spider is None:
            return "exploring"
        if spider.location.get_distance_to(NEST_POSITION) > NEST_SIZE * 3:
            return "exploring"
        return None

    def entry_actions(self):
        self.speed = 140. + randint(0, 350)

    def exit_actions(self):
        self.got_kill = False

def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    world = World()
    w, h = SCREEN_SIZE
    clock = pygame.time.Clock()
    print(clock)
    ant_image = pygame.image.load(".\pygame_test\\ant.png").convert_alpha()
    leaf_image = pygame.image.load(".\pygame_test\leaf.png").convert_alpha()
    spider_image = pygame.image.load(".\pygame_test\spider.png").convert_alpha()

    for ant_no in range(ANT_COUNT):
        ant = Ant(world, ant_image)
        ant.location = Vector2(randint(0, w), randint(0, h))
        ant.brain.set_state("exploring")
        # world.add_entity(ant)
        world[ant_no] = ant

    id = ANT_COUNT

    while True:
        for event in pygame.event.get():
            if event.type == 12:
                return
        time_passed = clock.tick(100)
    #
        if randint(1, 30) == 1:
            leaf = Leaf(world, leaf_image)
            leaf.location = Vector2(randint(0, w), randint(0, h))
            # world.add_entity(leaf)
            world[id] = leaf
            print('leaf', id)
            id += 1

    # #
        if randint(1, 100) == 1:
            spider = Spider(world, spider_image)
            spider.location = Vector2(-50, randint(0, h))
            spider.destination = Vector2(w + 50, randint(0, h))
            # world.add_entity(spider)
            world[id] = spider
            print('spider', id)
            id += 1
    #
        world.process(time_passed)
        world.render(screen)

        pygame.display.update()


if __name__ == "__main__":
    run()
