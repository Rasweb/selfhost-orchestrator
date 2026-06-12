export type Service = {
  id: string | number
  name: string
  status: 'online' | 'offline' | 'unknown'
  uptime?: string | null
  version?: string
  url?: string
}