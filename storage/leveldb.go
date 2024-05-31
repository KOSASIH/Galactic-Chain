package storage

import (
	"github.com/kezhuw/leveldb"
	"github.com/kezhuw/leveldb/filter"
	"github.com/kezhuw/leveldb/iterator"
)

type LevelDB struct {
	db *leveldb.DB
}

func NewLevelDB(db *leveldb.DB) *LevelDB {
	return &LevelDB{
		db: db,
	}
}

func (ldb *LevelDB) Put(key, value []byte) error {
	return ldb.db.Put(key, value, nil)
}

func (ldb *LevelDB) Get(key []byte) ([]byte, error) {
	return ldb.db.Get(key, nil)
}

func (ldb *LevelDB) Delete(key []byte) error {
	return ldb.db.Delete(key, nil)
}

func (ldb *LevelDB) NewIterator() iterator.Iterator {
	return ldb.db.NewIterator(nil, nil)
}

func (ldb *LevelDB) NewFilter() filter.Filter {
	return filter.NewBloomFilter(16)
}
