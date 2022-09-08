from gl import Raytracer, V3
from figures import *
from lights import *


width = 1024
height = 1024

# Materiales
snow = Material(diffuse = (1,1,1))
carbon = Material(diffuse = (0,0,0))
nariz = Material(diffuse = (1,0.4,0))
ojo = Material(diffuse = (0,0.66,0.89))
boca = Material(diffuse = (0.60,0.60,0.60))


rtx = Raytracer(width, height)

rtx.lights.append( AmbientLight( ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1) ))

#Cuerpo
rtx.scene.append( Sphere(V3(0,2,-8), 1.2, snow)  )
rtx.scene.append( Sphere(V3(0,0,-10), 2, snow)  )
rtx.scene.append( Sphere(V3(0,-2,-12), 3, snow)  )
#Carbon
rtx.scene.append( Sphere(V3(0,0,-5), 0.2, carbon)  )
rtx.scene.append( Sphere(V3(0,-0.9,-5), 0.2, carbon)  )
rtx.scene.append( Sphere(V3(0,-1.8,-5), 0.2, carbon)  )
#Cara
rtx.scene.append( Sphere(V3(0,1.4,-5), 0.2, nariz)  )
rtx.scene.append( Sphere(V3(0.3,1.7,-5), 0.1, ojo)  )
rtx.scene.append( Sphere(V3(-0.3,1.7,-5), 0.1, ojo)  )
rtx.scene.append( Sphere(V3(0.2,0.99,-5), 0.09, boca)  )
rtx.scene.append( Sphere(V3(-0.2,0.99,-5), 0.09, boca)  )
rtx.scene.append( Sphere(V3(0.3,1,-4), 0.09, boca)  )
rtx.scene.append( Sphere(V3(-0.3,1,-4), 0.09, boca)  )



rtx.glRender()

rtx.glFinish("output.bmp")