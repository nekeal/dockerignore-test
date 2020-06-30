import docker

client = docker.DockerClient(base_url='unix://var/run/docker.sock')


def build_image():
    image, build_output = client.images.build(path=f'git@github.com:nekeal/dockerignore-test.git',
                                              tag='dockerignore:test')
    for line in build_output:
        print(line.get('stream'))


if __name__ == '__main__':
    build_image()
