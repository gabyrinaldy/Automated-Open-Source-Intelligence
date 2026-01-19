# 🕵️‍♂️ AutoOSINT (Automated Open Source Intelligence)

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/status-active-success?style=for-the-badge)
![Category](https://img.shields.io/badge/category-Red%20Team-red?style=for-the-badge)

**Uma ferramenta modular em Python para automação da fase de reconhecimento em testes de intrusão.**

[Reportar Bug] • [Solicitar Feature]

</div>

---

## 📝 Sobre o Projeto

O **AutoOSINT** foi desenvolvido para agilizar a etapa de **Reconhecimento Passivo** (Information Gathering). Em vez de executar múltiplas ferramentas manuais, este script unifica a coleta de dados públicos sobre um alvo, permitindo que analistas de segurança foquem na análise e não na coleta.

Este projeto faz parte do meu portfólio de estudos em **Cibersegurança e Red Team**, demonstrando manipulação de APIs, sockets e estruturação de dados de inteligência.

Linkedin da criadora: www.linkedin.com/in/gabrielarinaldi02

🗺️ Roadmap
Melhorias planejadas para as próximas versões:

[ ] Implementar Port Scanning básico (Socket).

[ ] Adicionar suporte a argumentos via linha de comando (argparse).

[ ] Criar opção de salvar resultados em JSON para integração com outras ferramentas.

[ ] Dockerizar a aplicação.

## ✨ Funcionalidades

- [x] **WHOIS Lookup**: Identifica registrante, ASN e datas críticas do domínio.
- [x] **Passive Subdomain Enumeration**: Consulta logs de *Certificate Transparency* (crt.sh) para encontrar subdomínios sem gerar ruído direto no alvo.
- [x] **Email Harvesting**: Integração com API (Hunter.io) para mapear padrões de e-mail corporativos.
- [ ] **Tech Detection**: Identificação de CMS e tecnologias Web.
- [ ] **Report Generator**: Exportação automática para PDF/HTML.

## ⚙️ Pré-requisitos

Antes de começar, certifique-se de ter instalado:
* Python 3.8 ou superior
* Git

