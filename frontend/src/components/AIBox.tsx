export const AIBox = ({
  userinp,
  apiresponse,
}: {
  userinp: string;
  apiresponse: string;
}) => {
  return (
    <div
      className="z-20 w-3/5 h-3/5 max-h-64 border border-blue-500 flex items-center justify-center p-5 transition-all text-wrap overflow-hidden rounded-2xl"
      style={
        userinp !== ""
          ? {
              backdropFilter: "blur(2px)",
              boxShadow: "0 0 20px 8px rgba(0, 112, 243, 0.7)",
              backgroundColor: "rgba(0, 112, 243, 0.01)",
            }
          : {}
      }
    >
      {/* TODO: add isloading element */}
      <p className="silkscreen text-md">
        {apiresponse != "" ? apiresponse : "Waiting for response..."}
      </p>
    </div>
  );
};
