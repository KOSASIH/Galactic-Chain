import json
import os

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from galactic_chain.core.smart_contracts.ai_contract import AIContractEngine
from galactic_chain.utils.math.elliptic_curve_arithmetic import EllipticCurveArithmetic

app = Flask(__name__)
api = Api(app)

# Load AI Contract Engine
ai_contract_engine = AIContractEngine()

# Load Elliptic Curve Arithmetic
ecc = EllipticCurveArithmetic()


class GalacticChainAPI(Resource):
    def get(self):
        return {"message": "Welcome to the Galactic Chain API"}


class SmartContractAPI(Resource):
    def post(self):
        # Deploy new smart contract
        contract_code = request.json["contract_code"]
        contract_name = request.json["contract_name"]
        ai_contract_engine.deploy_contract(contract_code, contract_name)
        return {"message": f"Contract {contract_name} deployed successfully"}

    def get(self, contract_name):
        # Get contract details
        contract = ai_contract_engine.get_contract(contract_name)
        return {"contract": contract.to_dict()}


class TransactionAPI(Resource):
    def post(self):
        # Create new transaction
        sender = request.json["sender"]
        recipient = request.json["recipient"]
        amount = request.json["amount"]
        transaction = ai_contract_engine.create_transaction(sender, recipient, amount)
        return {"transaction": transaction.to_dict()}

    def get(self, transaction_id):
        # Get transaction details
        transaction = ai_contract_engine.get_transaction(transaction_id)
        return {"transaction": transaction.to_dict()}


class EllipticCurveAPI(Resource):
    def post(self):
        # Perform elliptic curve operation
        operation = request.json["operation"]
        params = request.json["params"]
        result = ecc.perform_operation(operation, params)
        return {"result": result}


api.add_resource(GalacticChainAPI, "/")
api.add_resource(SmartContractAPI, "/contracts", "/contracts/<string:contract_name>")
api.add_resource(
    TransactionAPI, "/transactions", "/transactions/<string:transaction_id>"
)
api.add_resource(EllipticCurveAPI, "/elliptic_curve")

if __name__ == "__main__":
    app.run(debug=True)
