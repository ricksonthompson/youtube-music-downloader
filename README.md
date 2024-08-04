# YouTube Music Downloader

Este script Python permite baixar músicas/áudios do YouTube a partir de links especificados em um arquivo JSON. Utiliza a biblioteca `yt-dlp` para o download e `ffmpeg` para a conversão de vídeos em arquivos de áudio MP3.

## Instalação

1. Clone o repositório:
    ```sh
    git clone git@github.com:ricksonthompson/youtube-music-downloader.git
    cd yt-music-downloader
    ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate   # No Windows, use: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Instale o `ffmpeg`:
    - No Windows: baixe e instale do [site oficial](https://ffmpeg.org/download.html).
    - No macOS: use `brew install ffmpeg`.
    - No Linux: use o gerenciador de pacotes da sua distribuição, por exemplo, `sudo apt-get install ffmpeg`.

## Uso

1. Preencha o arquivo [`urls.json`](/input/urls.json) no formato abaixo, contendo as URLs dos vídeos do YouTube que você deseja baixar e os nomes dos arquivos MP3:
    ```json
    [
      {
        "url": "https://www.youtube.com/watch?v=3jMqwdV0oWc",
        "name": "Eu escolho Deus"
      },
      {
        "url": "https://youtu.be/axKtfbZ7jIQ?si=5L0IirxV7IpfS6OY",
        "name": "Eu digo não"
      }
    ]
    ```

2. Execute o script:
    ```sh
    python src/yt_downloader_music.py
    ```

3. Os arquivos de áudio serão salvos no diretório atual com os nomes especificados no arquivo JSON.

## Dependências

- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://ffmpeg.org/download.html)
- [pydub](https://github.com/jiaaro/pydub)

## Contribuições

Sinta-se à vontade para abrir issues ou enviar pull requests. Todas as contribuições são bem-vindas!

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.