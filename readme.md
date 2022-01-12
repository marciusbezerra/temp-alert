
# Temp-Alert - Controle de temperatura do Raspberry

![Raspberry PI](https://www.electronicwings.com/public/images/user_images/images/Raspberry%20Pi/Raspberry%20Pi%20Introduction/Raspberry%20Pi%203%20hardware.png)

**Autor:**\
_Marcius Bezerra (adaptado)_\
_[marciusbezerra@gmail.com](mailto:marciusbezerra@gmail.com)_

## criando o serviço linux

```bash
sudo nano /etc/systemd/system/temp-alert.service
```

### Arquivo tem-alert.service

```text
[Unit]
Description=Temperature Alert Shutdown!! (Marcius)

[Service]
WorkingDirectory=/home/ubuntu/Projetos/temp-alert
ExecStart=/usr/bin/python3 /home/ubuntu/Projetos/temp-alert/temp-alert.py
Restart=always

[Install]
WantedBy=multi-user.target
```

## Ativando o serviço

```bash
sudo systemctl enable temp-alert.service
sudo systemctl start temp-alert.service
systemctl status temp-alert.service
```

## verificando os logs

```bash
tail -f temp-alert.log 
```
