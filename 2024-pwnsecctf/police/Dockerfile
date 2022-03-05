FROM clojure:tools-deps-1.11.4.1474-bullseye-slim

EXPOSE 3000

WORKDIR /src

ENV FLAG="PWNSEC{test_flag}"

COPY src/deps.edn ./

RUN clj

COPY src/app app
COPY src/resources resources

ENTRYPOINT ["clj", "-M", "-m", "core"]