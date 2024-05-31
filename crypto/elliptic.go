package crypto

import (
	"crypto/elliptic"
	"math/big"
)

func GenerateKeyPair() (*elliptic.CurveParams, *big.Int, *big.Int) {
	curve := elliptic.P256()
	privateKey, x, y, _ := elliptic.GenerateKey(curve, rand.Reader)
	return curve.Params(), privateKey, x, y
}
