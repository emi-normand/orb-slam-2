# orb-slam-2
## Backend
rendering is done using Open3D

## Bugs
When using WSL2, set the following
```
export LIBGL_ALWAYS_INDIRECT=0
export MESA_GL_VERSION_OVERRIDE=4.5
export MESA_GLSL_VERSION_OVERRIDE=450
export LIBGL_ALWAYS_SOFTWARE=1
```