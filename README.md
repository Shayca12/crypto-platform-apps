            ┌──────────────────────────┐
            │      GitHub Actions      │
            │   CI Build + Docker Push │
            └───────────┬──────────────┘
                        │
                        ▼
              DockerHub Images (Tagged)
                        │
                        ▼
    ┌────────────────────────────────────────┐
    │            GitOps Repository            │
    │ Helm Values Updated via Auto PR         │
    └───────────┬────────────────────────────┘
                │
                ▼
          ┌───────────────┐
          │    ArgoCD     │
          │ Auto Sync     │
          └──────┬────────┘
                 ▼
    ┌────────────────────────────────────────┐
    │ Kubernetes Cluster (Docker Desktop)     │
    │                                        │
    │  ┌──────────────┐    ┌──────────────┐  │
    │  │ auth-service │◄──►│ crypto-service│  │
    │  └──────────────┘    └──────────────┘  │
    │                                        │
    │ Ingress Routes:                         │
    │  /auth    → Auth Service                │
    │  /crypto  → Crypto Service              │
    └────────────────────────────────────────┘



---

## ⚙️ Tech Stack

| Category        | Tools Used |
|----------------|------------|
| Containers     | Docker |
| Orchestration  | Kubernetes |
| Deployment     | Helm Charts |
| CI/CD          | GitHub Actions |
| GitOps         | ArgoCD |
| External API   | CoinGecko |
| Cloud-Ready    | Designed for Production workflows |

---

## 📂 Repositories Structure

### Repo 1 — Application Services
`crypto-platform-apps`




Includes:

- Flask APIs
- Dockerfiles
- CI pipelines that build & push images

---

### Repo 2 — GitOps Deployment Repo
`crypto-platform-gitops`





Includes:

- Helm charts for Kubernetes deployments
- Environment-specific values
- ArgoCD Applications with Auto Sync

---

## 🚀 Features

✅ Token-based Authentication  
✅ Real-time Bitcoin/Ethereum prices  
✅ Microservice-to-microservice communication  
✅ CI pipelines with commit-based Docker tags  
✅ GitOps workflow with ArgoCD auto deployment  
✅ Professional API responses:

```json
{
  "coin": "bitcoin",
  "vs": "usd",
  "price": 68017,
  "source": "coingecko",
  "fetched_at": "2026-02-17T19:22:11Z"
}





