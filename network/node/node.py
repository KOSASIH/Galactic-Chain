from.node_service import NodeService
from.node_storage import NodeStorage

class Node:
    def __init__(self, node_id, node_service, node_storage):
        self.node_id = node_id
        self.node_service = node_service
        self.node_storage = node_storage

    def add_transaction(self, transaction):
        # Call node_service to validate and add transaction
        pass

    def add_block(self, block):
        # Call node_service to validate and add block
        pass
