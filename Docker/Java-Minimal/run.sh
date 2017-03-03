/usr/bin/docker run --rm -it \
                    --user=$(id -un) \
                    --volume="${HOME}:/mnt:rw" \
                    --workdir=/mnt/${PWD#${HOME}} \
                    --volume="/etc/group:/etc/group:ro" \
                    --volume="/etc/passwd:/etc/passwd:ro" \
                    java-minimal