from concurrency.blocking_queue import BoundedBlockingQueue
from concurrency.pipeline import PipelineStage

def test_pipeline():
    q1 = BoundedBlockingQueue(10)
    q2 = BoundedBlockingQueue(10)
    stage = PipelineStage(lambda x: x + 10, q1, q2)
    stage.start()
    q1.put(5)
    q1.put(None)
    assert q2.get() == 15
    assert q2.get() is None
