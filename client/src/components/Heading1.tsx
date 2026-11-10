interface Props {
  text: string
}

export default function Heading1(props: Props) {
  return (
    <h1 className="my-4 text-center text-5xl font-bold md:my-6">
      {props.text}
    </h1>
  )
}
