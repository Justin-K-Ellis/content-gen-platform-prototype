interface Props {
  text: string
}

export default function Heading2(props: Props) {
  return (
    <h1 className="mb-3 text-center text-3xl font-bold md:mb-4">
      {props.text}
    </h1>
  )
}
