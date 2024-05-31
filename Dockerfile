FROM golang:1.18 as builder

WORKDIR /app

COPY go.mod .
COPY go.sum .
RUN go mod download

COPY *.go .
RUN go build -o main .

FROM alpine:3.14

WORKDIR /app

COPY --from=builder /app/main /app/

EXPOSE 8080

CMD ["/app/main"]
