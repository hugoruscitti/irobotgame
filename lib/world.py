# -*- encoding: utf-8 -*-
import pyglet
from pyglet.gl import *

import config
import game

class World(pyglet.window.Window):

    def __init__(self):
        pyglet.window.Window.__init__(self, caption='I Robot ?', resizable=True) 
        self._scene = None
        self.change_scene(game.Game(self))
        self._init_window_size()
        self.enable_alpha_blending()

        if config.DEBUG:
            self.set_location(400, 400)
            self.fps = pyglet.clock.ClockDisplay()
        else:
            self.fps = None

    def run(self):
        pyglet.app.run()

    def change_scene(self, scene):
        if self._scene:
            self.pop_handlers()
            pyglet.clock.unschedule(self._scene.update)

        self._scene = scene
        self.push_handlers(scene)
        pyglet.clock.schedule_interval(scene.update, 1/60.0)

    def on_draw(self):
        self.fps.draw()

    def on_key_press(self, symbol, extra):
        if symbol == pyglet.window.key.F:
            self.set_fullscreen(not self.fullscreen)
        elif symbol in [pyglet.window.key.ESCAPE, pyglet.window.key.Q]:
            import sys
            sys.exit(0)











    # TODO: Llevar estas rutinas a otra clase abstracta, o extender "cocos.director".
    def _init_window_size(self):
        self._window_original_width = self.width
        self._window_original_height = self.height
        self._window_aspect =  self.width / float( self.height )
        self._offset_x = 0
        self._offset_y = 0

    def get_virtual_coordinates( self, x, y ):
        """Transforms coordinates that belongs the *real* window size, to the
        coordinates that belongs to the *virtual* window.

        For example, if you created a window of 640x480, and it was resized
        to 640x1000, then if you move your mouse over that window,
        it will return the coordinates that belongs to the newly resized window.
        Probably you are not interested in those coordinates, but in the coordinates
        that belongs to your *virtual* window. 

        :rtype: (x,y)           
        :returns: Transformed coordinates from the *real* window to the *virtual* window
        """

        x_diff = self._window_original_width / float( self.window.width - self._offset_x * 2 )
        y_diff = self._window_original_height / float( self.window.height - self._offset_y * 2 )

        adjust_x = (self.window.width * x_diff - self._window_original_width ) / 2
        adjust_y = (self.window.height * y_diff - self._window_original_height ) / 2

        return ( int( x_diff * x) - adjust_x,   int( y_diff * y ) - adjust_y )


    def on_resize( self, width, height):
        """Method that is called every time the main window is resized.
        
        :Parameters:
            `width` : Integer
                New width
            `height` : Integer
                New height
        """
        width_aspect = width
        height_aspect = int( width / self._window_aspect)

        if height_aspect > height:
            width_aspect = int( height * self._window_aspect )
            height_aspect = height

        self._offset_x = (width - width_aspect) / 2
        self._offset_y =  (height - height_aspect) / 2

        glViewport(self._offset_x, self._offset_y, width_aspect, height_aspect )
        glMatrixMode(gl.GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, self._window_original_width, 0, self._window_original_height, -1, 1)
        glMatrixMode(gl.GL_MODELVIEW)

        
    #
    # Misc functions
    #
    def enable_alpha_blending( self ):
        """Enables alpha blending in OpenGL using the GL_ONE_MINUS_SRC_ALPHA algorithm."""
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

