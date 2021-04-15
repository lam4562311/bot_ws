#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/robocon-dr1/bot_ws/src/rosserial/rosserial_xbee"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/robocon-dr1/bot_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/robocon-dr1/bot_ws/install/lib/python2.7/dist-packages:/home/robocon-dr1/bot_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/robocon-dr1/bot_ws/build" \
    "/usr/bin/python2" \
    "/home/robocon-dr1/bot_ws/src/rosserial/rosserial_xbee/setup.py" \
     \
    build --build-base "/home/robocon-dr1/bot_ws/build/rosserial/rosserial_xbee" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/robocon-dr1/bot_ws/install" --install-scripts="/home/robocon-dr1/bot_ws/install/bin"
