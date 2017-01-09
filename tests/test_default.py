import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
   '.molecule/inventory').get_hosts('all')


def get(e, nodeName):
    arg = r"./property[name='{nodename}']".format(nodename=nodeName)
    return e.find(arg)[1].text



def test_zookeeper_running(Service):
    service = Service('zookeeper')

    assert service.is_running
    assert service.is_enabled


def test_zookeeper_client_listening(Socket):
    socket = Socket('tcp://0.0.0.0:2181')
    assert socket.is_listening


def test_zookeeper_config(File):
    zoo_cfg = File('/etc/zookeeper/conf/zoo.cfg')
    assert f.exists
    assert f.user == 'zookeeper'
    assert f.group == 'zookeeper'
    assert f.mode == 0o644

    assert zoo_cfg.contains("dataDir=/var/lib/zookeeper")
    assert zoo_cfg.contains("dataLogDir=/var/log/zookeeper")
    assert zoo_cfg.contains("clientPort=2181")
    assert zoo_cfg.contains("initLimit=5")
    assert zoo_cfg.contains("syncLimit=2")
    assert zoo_cfg.contains("server.1=hdfs1:2888:3888")
