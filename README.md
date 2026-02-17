Run set -euo pipefail
Cloning into 'gitops'...
Switched to a new branch 'update-crypto-e84be0f'
[update-crypto-e84be0f 133acc1] Update crypto-service image tag to e84be0f
 1 file changed, 1 insertion(+), 1 deletion(-)
To https://github.com/***.git
 ! [rejected]        update-crypto-e84be0f -> update-crypto-e84be0f (non-fast-forward)
error: failed to push some refs to 'https://github.com/***.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
Error: Process completed with exit code 1.

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





