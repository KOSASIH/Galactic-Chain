use zk_snark::{G1, G2, Pairing};
use zk_snark::zk_snark::{Prover, Verifier};

struct ZKP {
    prover: Prover,
    verifier: Verifier,
}

impl ZKP {
   fn new() -> Self {
        let prover = Prover::new();
        let verifier = Verifier::new();
        ZKP { prover, verifier }
    }

    fn generate_proof(&self, statement: &[u8], witness: &[u8]) -> Vec<u8> {
        self.prover.generate_proof(statement, witness)
    }

    fn verify_proof(&self, statement: &[u8], proof: &[u8]) -> bool {
        self.verifier.verify_proof(statement, proof)
    }
}
