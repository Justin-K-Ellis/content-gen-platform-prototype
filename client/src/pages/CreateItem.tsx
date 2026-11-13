import { useParams } from "react-router"

export default function CreateItem() {
  const params = useParams()
  return <div>Create a {params.itemType?.toUpperCase()} item.</div>
}
