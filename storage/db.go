package storage

import (
	"fmt"
	"sync"

	"github.com/kezhuw/leveldb"
)

type DB struct {
	db   *leveldb.DB
	mu   sync.RWMutex
	path string
}

func NewDB(path string) (*DB, error) {
	db, err := leveldb.OpenFile(path, nil)
	if err != nil {
		return nil, err
	}
	return &DB{
		db:   db,
		path: path,
	}, nil
}

func (db *DB) Put(key, value []byte) error {
	db.mu.Lock()
	defer db.mu.Unlock()
	return db.db.Put(key, value, nil)
}

func (db *DB) Get(key []byte) ([]byte, error) {
	db.mu.RLock()
	defer db.mu.RUnlock()
	return db.db.Get(key, nil)
}

func (db *DB) Delete(key []byte) error {
	db.mu.Lock()
	defer db.mu.Unlock()
	return db.db.Delete(key, nil)
}

func (db *DB) Close() error {
	return db.db.Close()
}
